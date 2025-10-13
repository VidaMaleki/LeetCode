/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let s_set = new Set();
    let left = 0;
    let longSub = 0;
    for (let right = 0; right < s.length; right++){
        while (s_set.has(s[right])){
            s_set.delete(s[left])
            left ++;
        }
        s_set.add(s[right])
        longSub = Math.max(right - left+1, longSub);
        
    }
    return longSub;
};