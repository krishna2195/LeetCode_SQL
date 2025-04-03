# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        prev,cur=dummy,head
        while cur:
            if cur.next and cur.next.val==cur.val:
                while cur.next and cur.next.val==cur.val:
                    cur=cur.next
                prev.next=cur.next
            else:
                prev=prev.next
            cur=cur.next
        return dummy.next
        
        #Recursion T.C O(N) & S.C O(N)
        if not head or not head.next:
            return head
        if head.val==head.next.val:
            while head.next and head.val==head.next.val:
                head=head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next=self.deleteDuplicates(head.next)
            return head