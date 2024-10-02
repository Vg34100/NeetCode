from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # print(i)
            for j in range(i + 1, len(nums)):
                # print("  " + str(j))
                if nums[i] + nums[j] == target:
                    # print(str(nums[i]) + " + " + str(nums[j]))
                    return [i, j]

        
def main():
    sol = Solution()
    
    # Example 1
    nums = [3, 4, 5, 6]
    target = 7
    output = sol.twoSum(nums, target)
    print(output) # [0,1]
    
    # Example 2
    nums = [4, 5, 6]
    target = 10
    output = sol.twoSum(nums, target)
    print(output) # [0,2]
    
    # Example 3
    nums = [5, 5]
    target = 10
    output = sol.twoSum(nums, target)
    print(output) # [0,1]
    
    

if __name__ == "__main__":
    main()