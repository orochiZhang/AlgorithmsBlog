参考：[Sliding Window Algorithm(滑动窗口算法）分析与实践](https://www.jianshu.com/p/869f6d00d962)

例题：[最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：   
输入: S = "ADOBECODEBANC", T = "ABC"    
输出: "BANC"


```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(t) is None or len(s) is None:
            return ""
        
        # 计算每个字符的个数和字符串总长度
        t_dict = {}
        ABC = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        
        count = 0
        for char in ABC:
            n = t.count(char)
            if n > 0:
                t_dict[char] = n
                count += n
        
        # 记录最小的结果的下标和长度
        min_begin = -1
        min_end = -1
        min_num = -1
        
        # 记录s字符串中和t有关的字符的下标
        index = []
        # 记录s字符串中和t有关的字符的值
        strlist = []
        # 临时变量，字符的下标
        i = 0
        
        for char in s:
            if char in t_dict.keys():
                strlist.append(char)
                index.append(i)
            i += 1
            
        # s字符串中和t有关的字符集长度少过t的长度
        # 不可匹配，直接return
        length = len(t)
        # 记录s字符串中和t有关的字符的长度
        str_len = len(strlist)
        if str_len < length:
            return ""
            
        begin = 0
        end = 0 
        max_begin = str_len - length
        
        while end <= str_len and begin <= max_begin:
            isOK = True         # 记录是否成功匹配
            if end - begin < length:
                isOK = False
            else:
                if count > 0 :
                    isOK = False
                else:
                    pass
                
            if isOK:
                # 匹配成功，记录下标和长度
                num = index[end-1] - index[begin]
                if num < min_num or min_num == -1:
                    min_begin = begin
                    min_end = end-1
                    min_num = num
                    
                # 匹配成功，字符串头部指针向前推进
                # 尝试以更短的长度成功匹配
                k = strlist[begin]
                t_dict[k] += 1
                if t_dict[k] > 0:
                    count += 1 
                begin += 1
            else:
                # 匹配没成功，字符串尾部指针向前推进
                if end < str_len:
                    end += 1
                    k = strlist[end - 1]
                    t_dict[k] -= 1
                    if t_dict[k] >= 0:
                        count -= 1 
                else:
                # 最后字符串尾部指针已经指向最后一位字符串
                # 头部指针向前推进直到begin <= max_begin尝试以更短的长度成功匹配
                    k = strlist[begin]
                    t_dict[k] += 1
                    if t_dict[k] > 0:
                        count += 1 
                    begin += 1
        
        # 最后如果匹配成功，就返回结果    
        if min_num != -1:
            start = index[min_begin]
            end = index[min_end] + 1
            return s[start: end]
        else:
            return ""
```
