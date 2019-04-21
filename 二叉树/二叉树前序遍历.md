[leetcode-二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)

给定一个二叉树，返回它的前序遍历。     
示例:
```
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
```

思路：
1. 根节点入栈
2. 取出栈顶的节点放入结果List，把节点的右孩子，左孩子入栈。
3. 重复步骤2，直到栈为空，返回结果List
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        stack = []
        node = root
        stack.append(node)
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
```
