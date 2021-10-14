[设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/)

```python
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.data = []
        for i in range(k):
            self.data.append(None)
        self.num = 0
        self.len = k
        self.start = 0
        self.end = 0
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.num == self.len:
            return False
        self.data[self.start] = value
        self.num += 1
        if self.num == 1 and self.end + 1 != self.start:
            self.end += 1
            if self.end == self.len:
                self.end = 0
        self.start -= 1
        if self.start < 0:
            self.start = self.len - 1

        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.num == self.len:
            return False
        self.data[self.end] = value
        self.num += 1
        if self.num == 1 and self.start - 1 != self.end:
            self.start -= 1
            if self.start < 0:
                self.start = self.len - 1
        self.end += 1
        if self.end == self.len:
            self.end = 0
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.num == 0:
            return False
        self.start += 1
        if self.start == self.len:
            self.start = 0
        self.data[self.start] = None
        self.num -= 1
        if self.num == 0:
            self.end =self.start
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.num == 0:
            return False
        self.end -= 1
        if self.end < 0:
            self.end = self.len - 1
        self.data[self.end] = None
        self.num -= 1
        if self.num == 0:
            self.start = self.end
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.num == 0:
            return -1
        start = self.start + 1
        if start == self.len:
            start = 0
        return self.data[start]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.num == 0:
            return -1
        end = self.end - 1
        if end < 0:
            end = self.len - 1
        return self.data[end]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.num == 0 else False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return True if self.num == self.len else False
```
