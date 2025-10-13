/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let sumWindow = 0;
    let minSub = Infinity;
    let left = 0;
    for (let i = 0; i < nums.length; i++) {
        sumWindow += nums[i];
        while (sumWindow >= target) {
            minSub = Math.min(minSub, i-left+1);
            sumWindow -= nums[left++];
        }
    }
    return minSub === Infinity ? 0: minSub;

};