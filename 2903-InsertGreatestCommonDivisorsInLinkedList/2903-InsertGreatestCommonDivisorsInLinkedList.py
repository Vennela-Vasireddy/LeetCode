# Last updated: 11/15/2025, 6:24:20 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        gcd_list = ListNode(head.val) #gcd_list variable stores the address of the first node
        head_temp = head
        temp = gcd_list
        if head.next == None:
            return head
        while head is not None:
            if(head.next == None):
                break
            else:
                temp.next = ListNode(math.gcd(head.val, head.next.val))
                temp = temp.next
                temp.next = ListNode(head.next.val)
                temp = temp.next
                head =  head.next
        return gcd_list
            
        
        