from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for num in numbers:
            if target-num in  numbers:
                return [numbers.index(num)+1, numbers.index(target-num)+1]
            
def main():
    sol = Solution()
    
    # Example 1
    numbers = [1,2,3,4]
    target = 3
    
    output = sol.twoSum(numbers, target)
    print(output) # [1,2]

if __name__ == "__main__":
    main()