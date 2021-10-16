[另一个树的子树](https://leetcode-cn.com/problems/subtree-of-another-tree/)

给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:
```
     3
    / \
   4   5
  / \
 1   2
```
给定的树 t：
```
   4 
  / \
 1   2
```
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

## 解题思路
### 思路1
1. 层序遍历找到所有的和t根节点值相同的节点node，存放在c。c是一个列表
2. 记录t的层序遍历的结果
3. 遍历c的node，以node为根节点进行层序遍历
4. 对比用c的node的层序遍历结果和t的层序遍历结果对比，如果有一致返回True，否则返回False
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s and t:
            return False
        if not t:
            return True
        # 层序遍历找t的根节点
        c = []
        stack = [s]
        while stack:
            next_stack = []
            for node in stack:
                if node.val == t.val:
                    c.append(node)

                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            stack = next_stack
        if not c:
            return False

        # 层序遍历子树，判断是否与t的一致
        t_list = self.getTreeList(t)
        for node in c:
            c_list = self.getTreeList(node)
            if t_list == c_list:
                return True
        return False

    def getTreeList(self, head):
        tree_list = []
        stack = [head]
        while stack:
            next_stack = []
            for node in stack:
                tree_list.append(node.val)
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            stack = next_stack
        return tree_list
```

### 思路2
递归求解，代码看起来很绕

```python
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.t = t
        return self.func(s,t)
    
    def func(self,s,t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return self.func(s.left,self.t) or self.func(s.right,self.t)
        return self.func(s.left,t.left) and self.func(s.right,t.right) or self.func(s.left,t) or self.func(s.right,t)

```





