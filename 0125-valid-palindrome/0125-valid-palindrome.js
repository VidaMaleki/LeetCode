/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    
    let cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, "");
    let left = 0;
    let right = cleaned.length -1;
    console.log(cleaned)
    while (left < right) {
        if (cleaned[left]!== cleaned[right]){
            return false;
        }
        left++;
        right--;
    }
    return true;
};