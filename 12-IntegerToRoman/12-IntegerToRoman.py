# Last updated: 11/15/2025, 6:25:11 PM
class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
                }
        r = ''
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += Roman[n]
                num-=n
        return r
    
    
    
                

        
        
        
        
        
        