def shell_sort(arr):
    length = len(arr)
    step = length // 2      # 初始步长一般选择数组的一半长度
    while step > 0:
        i = 0
        while i < length:
            if i + step < length:
                print(step, "|", i, i+step, "|", arr[i], arr[i+step], arr[i] > arr[i+step])
                if arr[i] > arr[i+step]:
                    arr[i], arr[i + step] = arr[i + step], arr[i]
                    if i - step >= 0:
                        # 有交换，要和前一个数值进行比较
                        i -= step
                        continue
            i += step
        step = step // 2    # 步长减半，例如5->2->1->0结束循环
    return arr
   
arr = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
arr = shell_sort(arr)
print(arr)
