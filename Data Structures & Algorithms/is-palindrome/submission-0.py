class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for v in s:
            if v.isalpha():
                cleaned.append(v.lower())
            if v.isdigit():
                cleaned.append(v)
        front = 0
        end = len(cleaned) - 1
        while (front <= end):
            if not cleaned[front] == cleaned[end]:
                return False
            front += 1
            end -= 1
        return True