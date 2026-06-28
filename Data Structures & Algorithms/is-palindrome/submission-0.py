class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r'\W+', '', s).lower()

        if new_s == new_s[::-1]:
            return True
        return False

    
            

        