// Get all fields value
const hexCode = document.getElementById("hexCode");
const r = document.getElementById("r");
const g = document.getElementById("g");
const b = document.getElementById("b");
const previewBox = document.getElementById("previewBox");
const palette = document.getElementById("palette");

// IF PALETTE CHANGES
// Once palette changes, change first hexCode, then rgb code
function applyPalette() {
  hexCode.value = palette.value;
  changeRgbWithHex(hexCode.value);
}
// Event listener for palette
palette.addEventListener("change", applyPalette);

// IF RGB CODE CHANGES
// Once any of the rgb values changes,
// 1. validate them,
// 2. change hex color field (convert rgb to hex),
// 3. change preview background (using rgb)
// 4. and change palette (using newly found hex)
function checkRgbValues() {
  r.value = checkRgbFields(r.value);
  g.value = checkRgbFields(g.value);
  b.value = checkRgbFields(b.value);
  applyRgbToHex();
  applyRgbToPreview();
  applyHexToPalette();
}
function applyRgbToHex() {
  hexCode.value =
    "#" +
    componentToHex(r.value) +
    componentToHex(g.value) +
    componentToHex(b.value);
}
function applyRgbToPreview() {
  previewBox.style.background = `rgb(${r.value},${g.value},${b.value})`;
}
function applyHexToPalette() {
  palette.value = hexCode.value;
}
// Helper function to validate rgb fields upon input
function checkRgbFields(value) {
  if (value < 0) {
    return 0;
  } else if (value > 255) {
    return 255;
  } else {
    return parseInt(value);
  }
}
// Helper function to convert rgb components to hex
function componentToHex(c) {
  if (!c) {
    c = 0;
  }
  const hex = parseInt(c).toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}
// Function that checks if rgb values are <0 or nonexistent, and fixes them
function fixRgbNull(event) {
  if (!event.target.value || event.target.value < 0) {
    event.target.value = 0;
    return event.target.value;
  }
}
// Event listeners for rgb
r.addEventListener("focusout", () => fixRgbNull(event));
g.addEventListener("focusout", () => fixRgbNull(event));
b.addEventListener("focusout", () => fixRgbNull(event));

// IF HEX CODE CHANGES
// Once hex code is entered,
// 1. check if it is valid
// 2. change the preview background
// 3. check if it is a short code
function applyHex(value) {
  const isValidHexCode = /(^#[0-9A-F]{6}$)|(^#[0-9A-F]{3}$)/i.test(value);
  if (isValidHexCode) {
    changePreviewWithHex(value);
    if (value.length < 5) {
      // a. update Rgb fields using preview box;
      // b. update Hex using Rgb
      // c. update preview and palette;
      changeRgbWithHexShort();
      applyRgbToHex();
      applyRgbToPreview();
      applyHexToPalette();
    } else {
      // a. use Hex to find new Rgb
      // b. update palette using hex
      changeRgbWithHex(value);
      changePaletteWithHex(value);
    }
  }
}
// Check that the string is a valid hex code
function changePreviewWithHex(value) {
  previewBox.style.background = value;
}
// If the shorthand version of the hexcode is used, convert it into the long version
function changeRgbWithHexShort() {
  let previewBoxRgb = previewBox.style.background;
  let rgbArray = previewBoxRgb.slice(4, previewBoxRgb.length - 1).split(",");
  r.value = parseInt(rgbArray[0]);
  g.value = parseInt(rgbArray[1]);
  b.value = parseInt(rgbArray[2]);
}
// Once hex code is entered, update the rgb fields
function changeRgbWithHex(value) {
  r.value = hexToR(value);
  g.value = hexToG(value);
  b.value = hexToB(value);
}
// Helper functions to convert hex into rgb
function hexToR(h) {
  return parseInt(cutHex(h).substring(0, 2), 16);
}
function hexToG(h) {
  return parseInt(cutHex(h).substring(2, 4), 16);
}
function hexToB(h) {
  return parseInt(cutHex(h).substring(4, 6), 16);
}
function cutHex(h) {
  return h.charAt(0) == "#" ? h.substring(1, 7) : h;
}
// Change palette with hex
function changePaletteWithHex(value) {
  palette.value = value;
}

// Event listeners
hexCode.addEventListener("change", () => {
  applyHex(event.target.value);
});
