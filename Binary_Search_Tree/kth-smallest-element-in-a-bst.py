'''
二叉搜索树中第K小的元素
https: // leetcode-cn.com/problems/kth-smallest-element-in-a-bst/

二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，
或者是具有下列性质的二叉树：
若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值。

思路：
中序遍历二叉查找树可以得到从小到大的序列。
中序遍历，得到第K个数就是答案。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: 'TreeNode', k: 'int') -> 'int':
        stack = []
        out = []
        node = root
        n = 0
        while node is not None or len(stack) != 0:
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) != 0:
                node = stack[-1]
                stack = stack[:-1]
                out.append(node.val)
                node = node.right
                n += 1
                if n == k:
                    break
        return out[k-1]
