[删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)


双指针的思路：   
快指针先走N步，然后快指针和慢指针一步一步地走。    
当快指针走到结尾的时候，慢指针指向的地方就是该删除的节点。    
空间复杂度为O(1)   
注意判断：
1. 链表是否为空
2. 链表是否够长

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head     # 异常，链表为空
        fast = head
        slow = head
        pre = slow
        while n:
            if fast:
                fast = fast.next
            else:
                retun None  # 异常，链表不够长
            n -= 1
        
        while fast:
            print(fast.val, slow.val)
            pre = slow
            fast = fast.next
            slow = slow.next
            
        if pre is slow:
            head = slow.next
        else:
            pre.next = slow.next
        
        return head
```