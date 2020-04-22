# 二叉树前，中，后序的递归与非递归遍历
## 前序遍历
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
### 简洁递归
1. 前序遍历
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
        def visit(node):
            if not node:
                return 
            # ====前，中，后序区别仅在这三行的顺序====
            result.append(node.val)
            visit(node.left)
            visit(node.right)
            # =========
        visit(root)
        return result
```
2. 中序，后序遍历仅仅是改变visit函数的append顺序，不贴代码。

### 非递归思路
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

## 中序遍历
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
### 非递归思路
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

## 后序遍历
[leetcode-二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)     

给定一个二叉树，返回它的后序遍历。    
示例:
```
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
```
### 思路一
一直开始遍历节点的左孩子，入栈的时候记录每个节点的状态，1表示有右节点，0表示没有。出栈之前判断节点的状态，0就出栈。1就去遍历该节点的右节点，并把该节点状态置为0。
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        node = root
        while node is not None or len(stack) > 0:
            while node is not None:
                if node.right:
                    stack.append([node, 1])
                else:
                    stack.append([node, 0])
                node = node.left
                
            if len(stack) > 0:
                stack_node = stack[-1]
                if stack_node[1] == 1:
                    node = stack_node[0].right
                    stack[-1][1] = 0
                else:
                    result.append(stack_node[0].val)
                    stack.pop()
        return result
```
### 思路二
利用pre记录上一个访问过的结点，与当前结点比较，如果是当前结点的子节点，说明其左右结点均已访问，将当前结点出栈，更新pre记录的对象。
```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        node = root
        pop_node = None
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left
                
            if len(stack) > 0:
                stack_node = stack[-1]
                if stack_node.right:
                    if pop_node is stack_node.right:
                        result.append(stack_node.val)
                        pop_node = stack.pop()
                    else:
                        node = stack_node.right
                else:
                    result.append(stack_node.val)
                    pop_node = stack.pop()
        return result
```
### 思路三
取巧的方法。该写法的访问顺序并不是后序遍历，而是利用先序遍历“根左右”的遍历顺序，将先序遍历顺序更改为“根右左”，反转结果List（或者遍历的结果以入栈添加到结果List），得到结果顺序为“左右根”。
```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        if root is None:
            return result
        stack.append(root)
        while len(stack)>0:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            result.insert(0, node.val)
        return result
```

思路2,3参考leetcode的评论
