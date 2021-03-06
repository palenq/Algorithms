class Solution(object):  # O(n) : optimal as we need to traverse all n elems in worst case
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1

            if left < right and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
