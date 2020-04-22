## 验证回文
[验证回文串](https://leetcode-cn.com/problems/valid-palindrome)     
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。    
说明：本题中，我们将空字符串定义为有效的回文串。    
示例 1:
```
输入: "A man, a plan, a canal: Panama"
输出: true
```

### 正则骚操作
1. \w 匹配字母或数字或下划线或汉字 等价于 '[^A-Za-z0-9_]'。
2. 把\w以外的字符清除掉。并把所有字符转为小写。
3. 反转字符串，对比是否一致，一致就是回文。
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'\W','',s).lower()
        print(s)
        if s == s[::-1]:
            return True
        else:
            return False
```
