from typing import List


class Solution:

    def sameList(self, list1: List[int], list2: List[int]) -> bool:
        for listnum in list1:
            if listnum in list2:
                list2.remove(listnum)
            else:
                return False

        return True


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalList = list()
        templist = list()

        i = 0
        j = 1
        k = 2
        for num1 in nums:
            j = 1
            for num2 in nums[j:]:
                k = 2
                for num3 in nums[k:]:
                    if i != j != k != i:
                        # print(f"{i}, {j}, {k}")
                        if nums[i] + nums[j] + nums[k] == 0:
                            test = True
                            result = [num1, num2, num3]
                            # print(f"valid: {result}")
                            for temp in templist:
                                if self.sameList(temp, result.copy()):
                                    # print(f"but already exists...")
                                    test = False

                            if test:
                                templist.append(result)
                                finalList.append(result)

                    k += 1
                j += 1
            i += 1

        # print(finalList)
        return finalList
    
def main():
    sol = Solution()
    
    # Example 1
    nums = [-1,0,1,2,-1,-4]
    output = sol.threeSum(nums)
    print(output) # [[-1,-1,2],[-1,0,1]]
    
    # Example 2
    nums = [0,1,1]
    output = sol.threeSum(nums)
    print(output) # []
    
    # Example 3
    nums = [0,0,0]
    output = sol.threeSum(nums)
    print(output) # [[0,0,0]]
    
if __name__ == "__main__":
    main()