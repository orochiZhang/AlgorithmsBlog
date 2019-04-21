主要参考[阮一峰的网络日志-字符串匹配的KMP算法](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html)

```python
# 生成部分模式匹配表
def get_partial_match_table(T):
    TLength = len(T)
    TList = []
    for i in range(TLength):
        TList.append(0)
    for j in range(1, TLength):
        for k in range(0, TLength - j):
            if T[j + k] == T[0 + k]:
                TList[j + k] = k + 1
            else:
                break
    return TList


# S: 字符串主串
# T: 字符串模式串
def string_match(S:str , T:str):
    TList = get_partial_match_table(T)
    print(TList)
    Tlength = len(T)
    SLength = len(S)
    index = 0
    while (index + Tlength < SLength):
        # 成功匹配的字符数，每次匹配归零
        match_num = 0
        for i in range(Tlength):
            if T[i] == S[index + i]:
                match_num += 1
                if i == (Tlength - 1):
                    print(S)
                    print(' ' * index + T)
                    print(' ' * (index + i) + '^')
                    print('匹配成功')
                    return
            else:
                print(S)
                print(' ' * index + T)
                print(' ' * (index + i) + '^')
                # 字符串的位移 = 成功匹配的字符数 - 最后一次成功匹配的字符对应的部分匹配值
                n = match_num - TList[match_num - 1]
                print(match_num, '-', TList[match_num - 1], '=', n)
                # 如果n=0，移动一位
                if n > 0:
                    index += n
                else:
                    index += 1
                break
    print('匹配失败')

if __name__ == '__main__':
    string_match('ababcabcacbab', 'abcac')
    string_match('BBC ABCDAB ABCDABCDABDE', 'ABCDABD')
```
