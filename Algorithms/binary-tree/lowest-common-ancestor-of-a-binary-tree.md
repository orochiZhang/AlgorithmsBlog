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
