# Last updated: 11/15/2025, 6:24:57 PM
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s=''
        ans=''
        z=0
        c=0
        carry=0
        if(len(a)>=len(b)):
            z=len(a)-len(b)
            for x in range(z):
                s=s+'0'
            b=s+b
            
        else:
            z= len(b)-len(a)
            for x in range(z):
                s=s+'0'
            a=s+a
        for x in range(len(a)-1,-1,-1):
            c=carry
            if(int(a[x])+int(b[x])+c >=2 ):
                if(int(a[x])+int(b[x])+c==3):
                    ans='1'+ans
                    carry=1
                else:
                    ans='0'+ans
                    carry=1
            elif(int(a[x])+int(b[x])+c==1):
                ans = '1' + ans
                carry=0
            else:
                ans = '0'+ans
                carry=0
        if(carry==1): 
            ans=str(carry)+ans

        
        return ans
                    
                    
                
                
            
        
            
            
        