from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        longest = 0
        for num in nums:
            consecutive = 1
            while num+consecutive in nums:
                consecutive += 1
            if consecutive > longest:
                longest = consecutive

        return longest
    
    
def main():
    sol = Solution()
    
    # Example 1
    nums = [2,20,4,10,3,4,5]
    output = sol.longestConsecutive(nums)
    print(output) # 4
    
    # Example 2
    nums = [0,3,2,5,4,6,1,1]
    output = sol.longestConsecutive(nums)
    print(output) # 7
    
if __name__ == "__main__":
    main()
        