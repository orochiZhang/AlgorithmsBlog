# 二叉树的最近公共祖先

[二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

- 假设寻找节点p,q的共同祖先
- 从根节点开始向左右子树递归，深度搜索寻找节点p,q。
- 若左右各找到一个，那么当前根节点就是最近公共祖先，返回当前节点。
- 若只有左边找到，那么最近公共祖先在左边，返回左节点。
- 若只有右边找到，那么最近公共祖先在左边，返回右节点。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.p_path = []
        self.q_path = []
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
	        return None

        if root == p or root == q:
            return root
		
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None
```
- 二叉搜索树的特点，根节点比左节点大，比右节点小。
- 所以要找一个共同祖先，就是需要从根节点开始找，找到第一个node是要满足 min_node.val < node.val < max_node.val。
```
为什么是第一个node，看这个例子，如果寻找1， 6的共同祖先，我们需要的node是3，理论上4，5也是满足min_node.val < node.val < max_node.val。但是他们不是答案。
	 8
	/ \
   3   9
  / \
 1   4
    / \
   5   6
```
- 如果node大于max_node，那么就要从node.left寻找。
- 如果node小于min_node，那么就要从node.right寻找。
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