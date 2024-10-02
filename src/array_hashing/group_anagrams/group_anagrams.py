from typing import List


class Solution:

    def checkAnagram(self, string1, string2):
        if len(string1) != len(string2):
            return False
        if string1 == string2: return True

        for char1 in string1:
            if char1 not in string2:
                return False
            if string2.count(char1) != string1.count(char1):
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        finallist = []
        seen = set()
        for i, string1 in enumerate(strs):
            if string1 in seen:
                continue

            # print(f"next string1: {string1}")
            string1list = []
            string1list.append(string1)
            # print(string1list)
            seen.add(string1)
            for string2 in strs[i+1:]:
                if self.checkAnagram(string1, string2):
                    # print(f"{string1}, {string2}")
                    string1list.append(string2)
                    seen.add(string2)
            # print(f"string1list: {string1list}")
            # print(f"strs: {strs}")
            finallist.append(string1list)


                    

        # print(finallist)
        return finallist        

def main():
    sol = Solution()
    
    # Example 1
    strs = ["act","pots","tops","cat","stop","hat"]
    output = sol.groupAnagrams(strs)
    print(output) # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    
    # Example 2
    strs = ["x"]
    output = sol.groupAnagrams(strs)
    print(output) # [["x"]]
    
    # Example 3
    strs = [""]
    output = sol.groupAnagrams(strs)
    print(output) # [[""]]
    
    

if __name__ == "__main__":
    main()