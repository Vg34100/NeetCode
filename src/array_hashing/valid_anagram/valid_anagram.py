class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dicts = {}
        dictt = {}

        for char in s:
            if char in dicts:
                dicts[char] += 1
            else:
                dicts[char] = 1

        for char in t:
            if char in dictt:
                dictt[char] += 1
            else:
                dictt[char] = 1

        for key in dicts:
            if key in dictt:
                if dicts[key] != dictt[key]:
                    return False
            else:
                return False
        return True
    
def main():
    sol = Solution()
    
    s = "racecar"
    t = "carrace"
    output = sol.isAnagram(s, t)
    print(output)
    
    s = "jar"
    t = "jam"
    output = sol.isAnagram(s, t)
    print(output)
    

if __name__ == "__main__":
    main()
