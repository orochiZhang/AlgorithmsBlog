[最小栈](https://leetcode-cn.com/problems/min-stack/)

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。    
pop() -- 删除栈顶的元素。    
top() -- 获取栈顶元素。     
getMin() -- 检索栈中的最小元素。     

思路:     
每次入栈都入2个元素，一个是栈顶元素，一个是栈中最小值。    
每次出栈需要出2个元素。     
空间复杂度O(2n)
```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            self.stack.append(x)
        else:
            self.stack.append(x)
            if x < self.stack[-2]:
                self.stack.append(x)
            else:
                self.stack.append(self.stack[-2])

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-2]

    def getMin(self) -> int:
        return self.stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
