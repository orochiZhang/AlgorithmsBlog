# 二叉搜索树的最近公共祖先
[二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

- 二叉搜索树的特点: node.left.val < node.val < node.right.val 
- 假设p是较大的节点, q是较小的节点
- 思路：从根节点遍历。直到 q.val < node.val < p.val
- 如果node.val < q.val，node = node.right
- 如果node.val > p.val，node = node.left

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root

        max_node, min_node = (q, p) if q.val > p.val else (p, q)
        while node.val > max_node.val or node.val < min_node.val:
            if node.val > max_node.val:
                node = node.left
            elif node.val < min_node.val:
                node = node.right
        return node

```
