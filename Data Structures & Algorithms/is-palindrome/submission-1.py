class Solution:
    def isPalindrome(self, s: str) -> bool:
      mystring  = ""

      for char in s:
        if char.isalnum():
            mystring += char.lower()
      return mystring == mystring[::-1]      