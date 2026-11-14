class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip characters that are not letters or numbers
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True