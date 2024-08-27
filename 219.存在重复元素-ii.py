# @before-stub-for-debug-begin
from python3problem219 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #滑动窗口
        window = set()
        for i, num in enumerate(nums):
            if len(window) == k + 1:
                window.remove(nums[i - 1 - k])
            if num in window:
                return True
            window.add(num)
        return False
# @lc code=end

