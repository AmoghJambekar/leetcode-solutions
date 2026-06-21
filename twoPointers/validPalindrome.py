class Solution(object):
    def isPalindrome(self, s):
        cleaned = []
        for i in s:
            if i.isalnum():
                cleaned.append(i.lower())
        cleaned = "".join(cleaned)
        left = 0
        right = len(cleaned) - 1
        while left < right:
            if not(cleaned[left] == cleaned[right]):
                return False
            left += 1
            right -= 1
        return True
        