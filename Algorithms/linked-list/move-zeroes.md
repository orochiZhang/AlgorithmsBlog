leetcode原题：[移动零](https://leetcode-cn.com/problems/move-zeroes/)

示例:   
输入: [0,1,0,3,12]   
输出: [1,3,12,0,0]

图解思路：
当快指针指向的数字不为0的时候，把该数值赋值给慢指针指向的下标，然后慢指针+1。   
当快指针走完的时候，慢指针指向的下标开始，直到列表末尾，全部赋值0。
```
 sf
 || 
[0, 1, 0, 3, 12]
    sf
    ||
[1, 1, 0, 3, 12] 
    s  f
    |  |
[1, 1, 0, 3, 12] 
       s  f
       |  |
[1, 3, 0, 3, 12]
           s   f
           |   |
[1, 3, 12, 3, 12]

[1, 3, 12, 0, 0]
```

python代码：
```python
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = 0
    l = len(nums)
    for i in range(l):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1
    while k < l:
        nums[k] = 0
        k += 1
```
