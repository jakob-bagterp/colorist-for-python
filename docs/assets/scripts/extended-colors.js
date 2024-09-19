// Palette from colors.css converted from RGB to Hex:
const _black = '#030501';
const _brightWhite = '#fefefe';

function getTextColorFromBackgroundColor(hexColor) {
    function normalizeHexColorValue(hexColor) {
        // If the hex color code has a leading #, remove it, e.g. #0099CC to 0099CC.
        if (hexColor.slice(0, 1) === '#') {
            hexColor = hexColor.slice(1);
        }

        // If a hexcode has 3 charaters, convert it to 6 characters, e.g. 09C to 0099CC.
        if (hexColor.length === 3) {
            hexColor = hexColor.split('').map(function (hex) {
                return `${hex}${hex}`;
            }).join('');
        }
        return hexColor;
    }

    function convertHexColorToRgb(hexColor) {
        let red = parseInt(hexColor.substr(0, 2), 16);
        let green = parseInt(hexColor.substr(2, 2), 16);
        let blue = parseInt(hexColor.substr(4, 2), 16);
        return { red, green, blue };
    }

    function getYiqRatioFromRgb(red, green, blue) {
        return ((red * 299) + (green * 587) + (blue * 114)) / 1000;
    }

    hexColor = normalizeHexColorValue(hexColor);
    let { red, green, blue } = convertHexColorToRgb(hexColor);
	let yiqRatio = getYiqRatioFromRgb(red, green, blue);
	return (yiqRatio >= 128) ? _black : _brightWhite;
};

function setTextColorForTableCells() {
    function rgbToHex(rgb) {
        let result = rgb.match(/\d+/g).map(function(num) {
            let hex = parseInt(num).toString(16);
            return hex.length === 1 ? '0' + hex : hex;
        });
        return `#${result.join('')}`;
    }

    document.querySelectorAll('td.extended-colors').forEach(function(td) {
        let backgroundColor = window.getComputedStyle(td).backgroundColor;
        let hexColor = rgbToHex(backgroundColor);
        let textColor = getTextColorFromBackgroundColor(hexColor);
        td.style.color = textColor;
    });
}

setTextColorForTableCells();
