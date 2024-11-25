// Palette from colors.css converted from RGB to Hex:

const BLACK = '#030501';
const BRIGHT_WHITE = '#fefefe';

class RgbaColor {
    constructor(rgba) {
        this.rgba = rgba;
        let [red, green, blue, alpha] = rgba.match(/\d+/g).map(Number);
        this.red = red;
        this.green = green;
        this.blue = blue;
        this.alpha = alpha !== undefined ? alpha / 255 : 1;  // Normalize alpha to range [0, 1].
    }
}

function getTextHexColorInContrastToBackgroundColor(rgbaColor) {
    function getYiqRatio(rgbaColor) {
        return ((rgbaColor.red * 299) + (rgbaColor.green * 587) + (rgbaColor.blue * 114)) / 1000;
    }

	let yiqRatio = getYiqRatio(rgbaColor);
	return (yiqRatio >= 128) ? BLACK : BRIGHT_WHITE;
};

function setTextContrastColor() {
    document.querySelectorAll('*[class*="text-contrast"]').forEach(function(element) {
        let backgroundColor = new RgbaColor(window.getComputedStyle(element).backgroundColor);
        let textColorHex = getTextHexColorInContrastToBackgroundColor(backgroundColor);
        element.style.color = textColorHex;
    });
}

document$.subscribe(function() {
    setTextContrastColor();
})
