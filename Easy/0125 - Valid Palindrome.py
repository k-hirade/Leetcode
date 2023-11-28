class Solution:
    def isPalindrome(self, s: str) -> bool:
        # isalnum() : check if characters are alphanumeric
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        return filtered_s == filtered_s[::-1]
