from oauth2client.client import FlowExchangeError
from oauth2client.client import flow_from_clientsecrets
import httplib2
import json
import requests
import string
import random
from flask import Flask, render_template, jsonify, request, url_for, abort, g, redirect, flash
from flask import session as login_session
from flask import make_response
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from models import Base, User, Category, Color

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())[
    'web']['client_id']

engine = create_engine('sqlite:///colors.db',
                       connect_args={'check_same_thread': False})

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

# Create a state token to prevent request forgery.
# Store it in the session for later validation.
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # If a user is logged in, get current user info
    current_user = {}
    if 'username' in login_session:
        getCurrentUserInfo(current_user)
    return render_template('login.html', STATE=state, CLIENT_ID=CLIENT_ID, current_user=current_user)


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getCurrentUserInfo(current_user):
    # Get all current user's info
    current_user['username'] = login_session['username']
    current_user['picture'] = login_session['picture']
    current_user['email'] = login_session['email']
    current_user['id'] = login_session['user_id']
    return current_user

# GConnect
@app.route('/gconnect', methods=['POST'])
def gconnect():
  # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'appplication/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps(
            'Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = (
        'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # if there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access is used for the indended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps(
            "Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps(
            "Token's client ID does not match app's"), 401)
        print("Token's client ID does not match app's")
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check to see if user is already logged in
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = json.loads(answer.text)

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't, make a new one
    user_id = getUserID(data['email'])
    if not user_id:
        user_id = createUser(login_session)
        login_session['user_id'] = user_id
        print('New User Created!')
    else:
        print('User Already Exists')
        # login_session['user_id'] = user_id
        # user_info = getUserInfo(user_id)
        # print('User Found!')
    output = ''
    output += '<p>Welcome, '
    output += login_session['username']
    output += '!</p>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 200px; height: 200px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print("Login completed")
    return output
# End of gconnect


# DISCONNECT - Revoke a current user's token and reset their login_session.
@app.route("/gdisconnect")
def gdisconnect():
  # Only disconnect a connected user.
  # Check if a user is connected.
    try:
        access_token = login_session['access_token']
    except KeyError:
        access_token = None
    if access_token is None:
        response = make_response(json.dumps(
            'Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Execute HTTP GET request to revoke current token.
    url = "https://accounts.google.com/o/oauth2/revoke?token=%s" % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's session.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        # response = make_response(json.dumps('Successfully disconnected.'), 200)
        # response.headers['Content-Type'] = 'application/json'
        # return response
        flash('Successfully disconnected')
        return redirect(url_for("showLogin"))
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(json.dumps(
            'Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# API for categories
@app.route('/categories/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[c.serialize for c in categories])

# API for colors
@app.route('/colors/JSON')
def colorsJSON():
    colors = session.query(Color).all()
    return jsonify(colors=[c.serialize for c in colors])

# Show main page
@app.route('/')
@app.route('/categories')
def showCategories():
    categories = session.query(Category).all()
    for category in categories:
        colors = session.query(Color).filter_by(
            category_id=category.id).all()
        category.all_colors = colors
        creator = session.query(User).filter_by(
            id=category.user_id).one()
        category.creator = creator.name
    # If a user is logged in, get current user info
    current_user = {}
    if 'username' in login_session:
        getCurrentUserInfo(current_user)
    return render_template('categories.html', categories=categories, current_user=current_user)

# Show all colors belonging to a category
@app.route('/category/<int:category_id>/', methods=['GET', 'POST'])
def showColors(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    colors = session.query(Color).filter_by(
        category_id=category_id).all()
    # get info about the user, if logged in
    creator = getUserInfo(category.user_id)
   # If a user is logged in, get current user info
    current_user = {}
    if 'username' in login_session:
        getCurrentUserInfo(current_user)
    # If a user is not logged in, or the user logged in isn't the creator, return the public page
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('colorsPerCategoryPublic.html', colors=colors, category=category, creator=creator, current_user=current_user)
        # Else, return a page where s/he can fully edit the category
    else:
        return render_template('colorsPerCategory.html', category=category, colors=colors, creator=creator, current_user=current_user)

# Create a new category
@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    # If a user isn't logged in, it isn't possible to make a new category,
    # so redirect to login page
    if 'username' not in login_session:
        return redirect('/login')
    # If a user is logged in, get current user info
    current_user = {}
    if 'username' in login_session:
        getCurrentUserInfo(current_user)
    # If a request is sent, add a new category
    if request.method == 'POST':
        newCategory = Category(
            name=request.form['name'], user_id=login_session['user_id'])
        session.add(newCategory)
        flash('New Category "%s" Successfully Created' % newCategory.name)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html', current_user=current_user)

# Edit a category
@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(
        Category).filter_by(id=category_id).one()
    # Check if username is logged in, and if it is the same as the cretor of the category
    if 'username' not in login_session:
        return redirect('/login')
    # If a user is logged in, get current user info
    current_user = {}
    if 'username' in login_session:
        getCurrentUserInfo(current_user)
    if editedCategory.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this category.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category "%s" Successfully Edited' % editedCategory.name)
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category=editedCategory, current_user=current_user)

# Delete a category
@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(
        Category).filter_by(id=category_id).one()
    # Check if username is logged in, and if it is the same as the cretor of the category
    if 'username' not in login_session:
        return redirect('/login')
    # If a user is logged in, get current user info
    current_user = {}
    if 'username' in login_session:
        getCurrentUserInfo(current_user)
    if categoryToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this category.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        # Delete all colors inside of the category.
        # This will prevent these color to be reassigned by a new category
        # created afterwards that takes the same id of the deleted one
        colors = session.query(Color).filter_by(
            category_id=category_id).all()
        for color in colors:
            session.delete(color)
        # Delete category
        session.delete(categoryToDelete)
        flash('Category "%s" successfully deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete, current_user=current_user)

# Create a new color
@app.route('/category/<int:category_id>/color/new/', methods=['GET', 'POST'])
def newColor(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    # Chceck if a user is logged in
    if 'username' not in login_session:
        return redirect('/login')
    # If a user is logged in, get current user info
    current_user = {}
    if 'username' in login_session:
        getCurrentUserInfo(current_user)
    if request.method == 'POST':
        newColor = Color(name=request.form['name'], hex_code=request.form['hex_code'],
                         rgb_code="RGB(" + request.form['r'] + ", " + request.form['g'] + ", " + request.form['b'] + ")", category_id=category_id, user_id=category.user_id)
        session.add(newColor)
        session.commit()
        flash('New color "%s" Successfully Created' % (newColor.name))
        return redirect(url_for('showColors', category_id=category_id))
    else:
        return render_template('newColor.html', category_id=category_id, current_user=current_user)

# Edit a color
@app.route('/category/<int:category_id>/color/<int:color_id>/edit', methods=['GET', 'POST'])
def editColor(category_id, color_id):
    editedColor = session.query(Color).filter_by(id=color_id).one()
    # Chceck if a user is logged in
    if 'username' not in login_session:
        return redirect('/login')
    # If a user is logged in, get current user info
    current_user = {}
    if 'username' in login_session:
        getCurrentUserInfo(current_user)
    if request.method == 'POST':
        if request.form['name']:
            editedColor.name = request.form['name']
        if request.form['hex_code']:
            editedColor.hex_code = request.form['hex_code']
            editedColor.rgb_code = "RGB(" + request.form['r'] + ", " + \
                request.form['g'] + ", " + request.form['b'] + ")"
        session.add(editedColor)
        session.commit()
        flash('Color %s Successfully Edited' % editedColor.name)
        return redirect(url_for('showColors', category_id=category_id))
    else:
        rgbTuple = editedColor.rgb_code[4:len(
            editedColor.rgb_code)-1].split(",")
        r = int(rgbTuple[0])
        g = int(rgbTuple[1])
        b = int(rgbTuple[2])
        return render_template('editColor.html', category_id=category_id, color_id=color_id, color=editedColor, r=r, g=g, b=b, current_user=current_user)


# Delete a color
@app.route('/category/<int:category_id>/color/<int:color_id>/delete', methods=['GET', 'POST'])
def deleteColor(category_id, color_id):
    colorToDelete = session.query(Color).filter_by(id=color_id).one()
    # Chceck if a user is logged in
    if 'username' not in login_session:
        return redirect('/login')
    # If a user is logged in, get current user info
    current_user = {}
    if 'username' in login_session:
        getCurrentUserInfo(current_user)
    if request.method == 'POST':
        session.delete(colorToDelete)
        session.commit()
        flash('Color Successfully Deleted')
        return redirect(url_for('showColors', category_id=category_id))
    else:
        return render_template('deleteColor.html', category_id=category_id, color=colorToDelete, current_user=current_user)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
