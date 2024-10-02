from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = set()
        for i in range(k):
            mostfrequentindex = 0;
            mostfrequent = 0;
            for num in nums:
                if nums.count(num) > mostfrequent:
                    mostfrequent = nums.count(num)
                    mostfrequentindex = num
            final.add(mostfrequentindex)
            while mostfrequentindex in nums:
                nums.remove(mostfrequentindex)


        return list(final)

def main():
    sol = Solution()
    
    # Example 1
    nums = [1,2,2,3,3,3]
    k = 2
    output = sol.topKFrequent(nums, k)
    print(output) # [2, 3]
   
    # Example 2
    nums = [7, 7]
    k = 1
    output = sol.topKFrequent(nums, k)
    print(output) # [7] 
    

if __name__ == "__main__":
    main()