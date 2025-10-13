/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let sumWindow = nums.slice(0, k).reduce((a, b) => a + b, 0);
    let maxWindow = sumWindow / k;
    let left = 0;
    if (nums.length == k){
        return maxWindow;
    }
    for (let i = k; i < nums.length; i++){
        sumWindow += nums[i] - nums[left];
        left ++;
        let avgWindow = sumWindow / k;
        maxWindow = Math.max(maxWindow, avgWindow);
    }
    return maxWindow
};