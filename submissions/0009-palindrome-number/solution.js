/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let numStr = x.toString();
    let j = numStr.length - 1;
    for (let i = 0; i < numStr.length / 2; i++){
        if (numStr[i] !== numStr[j]){
            return false;
        }
        j--
    }
    return true;
};


