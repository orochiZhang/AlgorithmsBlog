[二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)    
给定二叉树 [3,9,20,null,null,15,7]，返回它的最大深度 3 。
```
    3
   / \
  9  20
    /  \
   15   7
```

## 递归思路

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l1 = self.maxDepth(root.left)
        l2 = self.maxDepth(root.right)
        l = max(l1,l2)
        return l+1
``` 

## 非递归思路
1. 构建一个先进先出的队列。
2. 记录每一层最后一个节点end，第一层end是root。
3. 层序遍历，队列pop一个节点，把节点的子节点加到队列。
4. 每次pop一个节点，判断该元素是否是节点end，如果是，depth加一。选取队列尾部的节点为新的节点end。
5. 当队列为空，返回depth。


end |   |end |    |end| 
--- |---|--- |--- |---|
3   | 9 | 20 | 15 | 7 |


```python
class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        depth = 0
        queue = [root]
        end = root
        while queue:
            p = queue.pop(0)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
            if p == end:
                depth += 1
                if queue:
                    end = queue[-1]
        return depth
```
