from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        while strs:
            string = string + strs.pop(0) + "|"
        # print(string)
        return string
        
    def decode(self, s: str) -> List[str]:
        finallist = []
        word = ""
        for char in s:
            if char == '|': # A little bit cheatsy
                finallist.append(word)
                word = ""
            else: 
                word += char
            
        return finallist

def main():
    sol = Solution()
    
    # Example 1
    input = ["neet","code","love","you"]
    
    encoded = sol.encode(input)
    print(encoded) # neet|code|love|you|

    decoded = sol.decode(encoded)
    print(decoded) # ['neet', 'code', 'love', 'you']
    
    # Example 2
    input = ["we","say",":","yes"]
    
    encoded = sol.encode(input)
    print(encoded) # we|say|:|yes|

    decoded = sol.decode(encoded)
    print(decoded) # ['we', 'say', ':', 'yes']
    
if __name__ == "__main__":
    main()