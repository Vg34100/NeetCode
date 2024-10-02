class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s.lower():
            if char.isalnum():
                newStr += char

        # print(f"new string:{newStr}.")
        length = len(newStr)

        for i in range(length):
            if newStr[i] != newStr[length-1-i]:
                return False
        return True

def main():
    sol = Solution()
    
    # Example 1
    s = "Was it a car or a cat I saw?"
    output = sol.isPalindrome(s)
    print(output) # True
    
    # Example 2
    s = "tab a cat"
    output = sol.isPalindrome(s)
    print(output) # False
    
if __name__ == "__main__":
    main()