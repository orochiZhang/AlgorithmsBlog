Boyer-Moore majority vote algorithm (摩尔投票算法)是一种在线性时间O(n)和空间复杂度的情况下，在一个元素序列中查找包含最多的元素。它是以Robert S.Boyer和J Strother Moore命名的，1981年发明的，是一种典型的流算法(streaming algorithm)。

### 算法思想
1. 极限1换1，遇到相同的元素+1，遇到不同的元素-1
2. 如果该元素的数量超过元素序列总和的一半以上，那么最后留下的就是该元素。

### 相关的leetcode题目
1. [多数元素](https://leetcode-cn.com/problems/majority-element/)
2. [数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)
3. [求众数II](https://leetcode-cn.com/problems/majority-element-ii/)

**多数元素，数组中出现次数超过一半的数字题目要求**：
1. 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
2. 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

python代码：
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for value in nums:
            if count == 0:
                candidate = value
            if candidate == value:
                count += 1
            else:
                count -= 1
        
        return candidate if nums.count(candidate) > (len(nums)/2) else None
```

**求众数II**   
需求从求超过一半的元素变成求两个超过1/3的元素，但是核心思想并没有变。
1. 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
2. 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

Python代码:
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        for value in nums:
            if count1 == 0 and value != candidate2:
                candidate1 = value
                count1 = 1
            elif count2 == 0 and value != candidate1:
                candidate2 = value
                count2 = 1

            elif candidate1 != value and candidate2 != value:
                count1 -= 1
                count2 -= 1
            elif candidate1 == value:
                count1 += 1
            elif candidate2 == value:
                count2 += 1

        candidate1 = candidate1 if nums.count(candidate1) > (len(nums)//3) else None
        candidate2 = candidate2 if nums.count(candidate2) > (len(nums)//3) else None
        result = []
        if not candidate1 is None and count1:
            result.append(candidate1)
        if not candidate2 is None and count2:
            result.append(candidate2)
        return result
```

### 并行优化
求众数其实有个简单暴力的解法，先排序，然后取中间元素。但是这种解法不适合海量数据的情况。
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums)//2]
```

Boyer-Moore majority vote algorithm 面对海量数据的情况可以使用并行算法实现。    
基本思想如下：
1. 把数组元素分割为若干份，长度不要求统一。
2. 用Boyer-Moore majority vote algorithm 求出每个数组的最多的元素，数量。
3. 对比每个数组的元素，数量，得到最终结果。

简单例子：  
原数组为 [1,1,0,1,1,0,1,0,0]   
划分计算：   
[1,1,0,1,1] –> (1,3)   
[0,1,0,0] –> (0,2)  
对比，最终结果是1。

面对上百GB的数据，Boyer-Moore majority vote algorithm可以采用 MapReduce 的方式来解决这个问题。而“先排序，然后取中间元素”的暴力解法是不行。

### 参考文献
- [Finding the Majority Element in Parallel](http://www.crm.umontreal.ca/pub/Rapports/3300-3399/3302.pdf)
- [多数投票算法(Boyer-Moore Algorithm)详解](https://blog.csdn.net/kimixuchen/article/details/52787307)
