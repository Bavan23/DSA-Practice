class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  
            return False
        
        rev = 0
        temp = x
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10
        
        return x == rev
    

num=int(input("Enter a Number: "))
check=Solution()
print(check.isPalindrome(num))
