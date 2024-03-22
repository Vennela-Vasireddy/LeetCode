class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left_height = []
        Right_height = []
        for x in range(0, len(height)):
            left_height.append(max(height[0:x+1]))
            Right_height.append(max(height[x:len(height)]))
        for x in range(len(height)):
            water +=min(left_height[x], Right_height[x]) -height[x]
        return water
            
            
            
        
        
#     #Below solution is Brute Force which exceeds time
#         water,i,j,x,y = 0,0,len(height)-1,0,len(height)-1
#     # removing zeroes at the end and begining
#         def fun(i, j):
#             x,y = 0,0
#             while(i!=len(height)):
#                 if(height[i]>0):
#                     x=i
#                     break
#                 i=i+1
#             while(j!=-1):
#                 if(height[j]>0):
#                     y=j
#                     break
#                 j=j-1
#             return x,y
        
#         n =  max(height)
# #iterating over to find the blocks to store rain
#         while(n>0):
#             x,y = fun(i,j)
#             duplicate_height = set(height[x:y+1])
#             if(min(duplicate_height)==0):
#                 duplicate_height.remove(min(duplicate_height))
#             for z in range(x, y+1):
#                 if height[z] < min(duplicate_height):
#                     water += min(duplicate_height) - height[z]
#                     height[z] = 0
#                 else:
#                     height[z] = height[z] - min(duplicate_height)
#             i = x
#             j = y
#             n = n-min(duplicate_height)
#         return water

        