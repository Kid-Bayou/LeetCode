/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let key = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    let value = 0;

    for (let i = 0; i < s.length; i++) {
        const curr = key[s[i]];
        const next = key[s[i+1]];

        if (curr < next) {
            value += next - curr;
            i++;
        }
        else {
            value += curr;
        }
    }
    return value;
};
