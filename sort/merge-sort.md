## 递归-归并排序
```python
# 归并排序
def merge_sort(arr):
    length = len(arr)
    if length > 3:
        middle = length // 2
        arr1 = merge_sort(arr[:middle])
        arr2 = merge_sort(arr[middle:])
        return arr_sort(arr1, arr2)
    else:
        return bubble_sort(arr)

# 冒泡排序
def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i, length):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# 合并数组
def arr_sort(arr1, arr2):
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)
    arr = []
    while i < len1 or j < len2:
        if i < len1 and j < len2:
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
        elif i < len1:
            arr.extend(arr1[i:])
            i = len1
        elif j < len2:
            arr.extend(arr2[j:])
            j = len2
    return arr


arr = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
arr = merge_sort(arr)
print(arr)
```
