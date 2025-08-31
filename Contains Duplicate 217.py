from typing import List

class Solution:
    def containsDuplicate(nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
