class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            # Move the pointers if they are not alphanumeric chars
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # Return false on the basis the alphanumeric chars are not equal
            if s[l].lower() != s[r].lower():
                return False
            # Keep moving both ptrs toward the middle as we successfully compare
            # both ends of the string
            l += 1
            r -= 1
        return True