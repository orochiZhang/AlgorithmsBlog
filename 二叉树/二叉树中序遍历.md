[leetcode-二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

给定一个二叉树，返回它的中序遍历。    
示例:
```
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
```
思路：
1. 对于任一结点，首先把其放入栈，然后访问其左孩子，而左孩子结点又可以看做一根结点，然后继续访问其左孩子结点，直到遇到左孩子结点为空的结点才进行访问栈顶。
2. 从栈顶获取到的节点，把该节点放入结果List，如果该节点有右节点，那么对其右子树做步骤1的操作。
3. 直到栈为空，遍历结束，返回结果List。
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        stack = []
        result = []
        node = root
        while (node is not None) or (len(stack) != 0):
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) != 0:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result
```
