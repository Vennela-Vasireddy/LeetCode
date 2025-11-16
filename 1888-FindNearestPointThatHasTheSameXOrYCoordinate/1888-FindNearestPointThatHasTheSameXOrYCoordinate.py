# Last updated: 11/15/2025, 6:24:30 PM
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        l=0
        d={}
        if (len(points)==1):
            if(points[0][0]==x or points[0][1]==y):
                return 0
            else:
                return -1
        for z in range(0,len(points)):
            if(points[z][0]==x or points[z][1]==y):
                d[z] = abs(x-points[z][0])+abs(y-points[z][1])
        if(d=={}):
            return -1
        else:
            return min(d, key=d.get)
                
                
            
        
        