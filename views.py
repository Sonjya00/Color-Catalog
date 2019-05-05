from models import Base, User, Category, Color
from flask import Flask, render_template, jsonify, request, url_for, abort, g, redirect, flash
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

engine = create_engine('sqlite:///colors.db',
                       connect_args={'check_same_thread': False})

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

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
    return render_template('categories.html', categories=categories)

# Show all colors belonging to a category
@app.route('/category/<int:category_id>/', methods=['GET', 'POST'])
def showColors(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    # creator = getUserInfo(category.user_id)
    colors = session.query(Color).filter_by(
        category_id=category_id).all()
    # if 'username' not in login_session or creator.id != login_session['user_id']:
    #     return render_template('publiclist.html', items=items, category=category, creator=creator)
    # else:
    #     return render_template('publiclist.html', items=items, category=category, creator=creator)
    return render_template('colorsPerCategory.html', category=category, colors=colors)

# Create a new category
@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    # if 'username' not in login_session:
    #     return redirect('/login')
    if request.method == 'POST':
        newCategory = Category(
            name=request.form['name'], user_id=request.form['user_id'])
        session.add(newCategory)
        flash('New Category %s Successfully Created' % newCategory.name)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')

# Edit a category
@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    # if 'username' not in login_session:
    #     return redirect('/login')
    editedCategory = session.query(
        Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category Successfully Edited %s' % editedCategory.name)
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category=editedCategory)

# Delete a category
@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(
        Category).filter_by(id=category_id).one()
    # if 'username' not in login_session:
    #     return redirect('/login')
    # if categoryToDelete.user_id != login_session['user_id']:
    #     return "<script>function myFunction() {alert('You are not authorized to delete this category. Please create your own category in order to delete.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(categoryToDelete)
        flash('%s Successfully Deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    #app.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    app.run(host='0.0.0.0', port=8000)
