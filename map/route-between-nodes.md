leetcode : [节点间通路](https://leetcode-cn.com/problems/route-between-nodes-lcci/)

给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:
```
 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 输出：true
```

解题思路
1. DFS深度搜索，不过如果从start开始深度搜索，最后一个测试用例数据量大，因为超时而无法通过。
2. 改变一下思路，从target开始深度搜索找start。

python代码
```python
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        result = False
        for path in graph:
            x, y = path
            if y == target:
                result = self.dfs(graph, x, start, [x, y])
            if result:
                return result
        return result
    
    def dfs(self,  graph: List[List[int]], node: int, target: int, path: List):
        result = False
        if target == node:
            return True
        for path_list in graph:
            x, y = path_list
            if y == node and x not in path:
                path.append(node)
                result = self.dfs(graph, x, target, path)
            if result:
                return result
        return result
```

通过后，我写的DFS速度才50%，看了一下速度90%的代码。
1. 思路是BFS
2. 这段代码要求graph的数据是从0开始递增（该题的用例数据都是从0开始递增）
3. 如果乱序，需要对graph的数据排序
```python
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        a=set([start])

        for i in graph:
            if i[0] in a:
                a.add(i[1])
            if target in a:
                return True
        return False
```

