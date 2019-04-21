[leetcode-二叉树的层次遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:   
给定二叉树: [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
返回其层次遍历结果：
```
[
  [3],
  [9,20],
  [15,7]
]
```
思路：
1. 根节点入队列
2. 遍历队列，把节点的值加入结果List，同时把栈的节点的左右孩子都添加到下一个队列。
3. 重复步骤2，直到队列为空，返回二维的结果List。
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if root is None:
            return []
        rank = []
        result = []
        rank.append(root)
        while(len(rank) != 0):
            next_rank = []
            result_list = []
            for item in rank:
                result_list.append(item.val)
                if item.left:
                    next_rank.append(item.left)
                if item.right:
                    next_rank.append(item.right)
            result.append(result_list)
            rank = next_rank
        return result
```
