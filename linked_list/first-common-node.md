[两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)

思路：   
1. 两个链表一起遍历，得到两个链表的长度。
2. 计算链表的长度差N。
3. 长的链表先走N步。
4. 两个链表一起走，判断是否有交点。


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 计算长度
        numA = 0 
        numB = 0
        nodeA = headA
        nodeB = headB
        while nodeA:
            numA += 1
            nodeA = nodeA.next
        while nodeB:
            numB += 1
            nodeB = nodeB.next
        
        # 长的链表先走N步
        nodeA = headA
        nodeB = headB
        while numB > numA:
            nodeB = nodeB.next
            numB -= 1
        while numA > numB:
            nodeA = nodeA.next
            numA -= 1
        
        # 找交点
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeB = nodeB.next
            nodeA = nodeA.next
        return None
```
