class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x==0:
            return True
        elif x>0:
           sol=str(x)
           sol1_1=sol[::-1]
           if sol==sol1_1:
             return True
           else:
            return False
        