class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        if x / 10 == 0:
            return True
        
        is_palindrome = True
        
        base = 1
        
        while x / base >= 10:
            base *= 10
        
        while x:
            left_digit = x / base
            right_digit = x % 10
            
            if left_digit != right_digit:
                is_palindrome = False
                break
            
            x -= base * right_digit
            x = x / 10
            base = base / 100
                
        return is_palindrome