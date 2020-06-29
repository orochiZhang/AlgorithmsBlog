[leetcode-排序数组](https://leetcode-cn.com/problems/sort-an-array/)

## 快排递归
最容易理解的快排递归版本，性能较差。
```python
def qsort(arr):
    if not len(arr):
        return []
    else:
    # 在这里以第一个元素为基准线
        pivot = arr[0]
        left = qsort([x for x in arr[1:] if x < pivot])
        right = qsort([x for x in arr[1:] if x >= pivot])
    return left+[pivot]+right

arr = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
arr = qsort(arr)
print(arr)
```

## 快排非递归
递归转换为非递归，主要的思路就是使用栈来模拟递归的顺序。
```python
def qsort_by_stack(arr):
    if not len(arr):
        return []
    else:
        left = 0
        right = len(arr) - 1
        stack = []
        stack.append(left)
        stack.append(right)
        while stack:
            right = stack.pop()
            left = stack.pop()
            
            index = qsort2(arr, left, right)
            print(index)
            if index-1 > left:
                stack.append(left)
                stack.append(index-1)
            if index+1 < right:
                stack.append(index+1)
                stack.append(right)
    return arr
        
def qsort2(arr, start, end):
    pivot = arr[end]
    left, right = start, end
    while left < right:
        while (left < right and arr[left] <= pivot):
            left += 1
    
        while (left < right and arr[right] >= pivot):
    
            right -= 1
        arr[right], arr[left] = arr[left], arr[right]
    arr[end], arr[left] = arr[left], arr[end]
    return left

arr = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
arr = qsort_by_stack(arr)
print(arr)
```
