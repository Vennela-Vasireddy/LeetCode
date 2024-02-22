# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length_head = head
        copy_head = head
        length = 0
        i = 0
        while(length_head):
            length +=1
            length_head=length_head.next
        index_to_delete = length - n
        if(index_to_delete == 0):
            return head.next
        while(i<index_to_delete-1):
            print (copy_head.val)
            copy_head = copy_head.next
            i+=1
        copy_head.next = copy_head.next.next
        return head
        