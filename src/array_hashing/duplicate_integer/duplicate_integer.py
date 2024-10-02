# Duplicate Integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num in dict:
                return True
            dict[num] = True
        return False
    

def main():
    nums = [1, 2, 3, 3]
    
    sol = Solution()
    output = sol.hasDuplicate(nums)
    
    print(output)

if __name__ == "__main__":
    main()