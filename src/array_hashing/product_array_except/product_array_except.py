from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finallist = []
        for num in nums:
            testnums = nums.copy()
            testnums.remove(num)
            product = testnums[0]
            for testnum in testnums[1:]:
                product *= testnum
            finallist.append(product)
        return finallist

def main():
    sol = Solution()
    
    # Example 1
    nums = [1, 2, 4, 6]
    output = sol.productExceptSelf(nums)
    print(output) # [48,24,12,8]
    
    # Example 2
    nums = [-1, 0, 1, 2, 3]
    output = sol.productExceptSelf(nums)
    print(output) # [0,-6,0,0,0]
    
if __name__ == "__main__":
    main()