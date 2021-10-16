leetcode原题：[验证栈序列](https://leetcode-cn.com/problems/validate-stack-sequences/submissions/)

给定 pushed 和 popped 两个序列，每个序列中的值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

示例 1：
```
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```
思路：
1. 模拟一遍出栈，用变量j表示成功模拟出栈的个数。  
2. 先把pushed的一个元素进栈，然后检验栈顶元素是否和popped[j]一致。
3. 如果一致，出栈，j+1。
4. 最后检验j是否等于popped的长度。   

python代码：
```python
def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    j = 0
    s = []
    for x in pushed:
        s.append(x)
        while s and j < len(popped) and s[-1] == popped[j]:
            s.pop()
            j += 1
    return j == len(popped)
