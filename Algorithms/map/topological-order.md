## 概念
首先要理解几个概念：
1. **有向无环图**(DAG)：指的是一个无回路的有向图。
2. **顶点活动网**(Activity On Vertex network)，简称AOV网。
   一个大型工程一般会划分若干个子工程，为了形象地反映出整个工程中各个子工程(活动)之间的先后关系，可以用一个有向图来表示。图的顶点代表子工程(活动)，图的有向边代表活动的先后关系。通常，我们把这种顶点表示活动、边表示活动间先后关系的有向图称为顶点活动网。
3. 一个**顶点活动网**应该是一个有向无环图，即不应该带有回路，因为若带有回路，则回路上的所有活动都无法进行。
4. **拓扑序列**(Topological order)，在**顶点活动网**中，若不存在回路，则所有子工程(活动)可排列成一个线性序列，使得每个活动的所有前驱活动都排在该活动的前面，我们把此序列叫做拓扑序列。
5. **拓扑排序**（Topological sort）由AOV网构造拓扑序列的过程叫做**拓扑排序**。AOV网的拓扑序列不是唯一的，满足上述定义的任一线性序列都称作它的拓扑序列。
6. 拓扑序列的实际意义是：如果按照拓扑序列中的顶点次序，在开始每一项活动时，能够保证它的所有前驱活动都已完成，从而使整个工程顺序进行，不会出现冲突的情况。
7. 顶点的**度**(degree)，就是指和该顶点相关联的边数。在有向图中，度又分为**入度**和**出度**。
8. **入度** (in-degree) ：以某顶点版为弧头，终止于权该顶点的弧的数目称为该顶点的入度。
9. **出度** (out-degree) ：以某顶点为弧尾，起始于该顶点的弧的数目称为该顶点的出度。

## 拓扑排序
1. 统计图中每个节点的入度，生成**入度表**in-degree。
2. 构建邻接表，记录每一个节点的所有邻接节点。
3. 构建一个空列表为拓扑顺序列表。
4. 用一个队列 queue，将所有入度为 0 的节点入队。
5. 当 queue 非空时，依次将队首节点node出队：
    1. 节点node的所有邻接节点的入度 - 1。
    2. 检查邻接节点入度是否为0，如果是，加入队列。
    3. 拓扑顺序列表加入节点node
6. 当 queue 非空时，拓扑顺序列表的节点数如果是和图的节点数相同，则该图是一个**顶点活动网**（AOV网），该拓扑顺序表是其中一种拓扑序列。

## leetcode题目
### 1. 课程表问题
https://leetcode-cn.com/problems/course-schedule

你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。    
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]   
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

示例 1:  
输入: 2, [[1,0]]   
输出: true  
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。 

```python
class Solution:
    def __init__(self):
        self.state = {}

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]      # 入度表
        adjacency = [[] for _ in range(numCourses)]     # 邻接表
        queue = [] 
        # 计算入度
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # 把入度为0的节点加入队列
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
    
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
        # 如果numCourses = 0，说明该图是有拓扑序列。
        return not numCourses
```

### 2. 课程表II
https://leetcode-cn.com/problems/course-schedule-ii/

现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:    
输入: 2, [[1,0]]    
输出: [0,1]   
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。   
```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]      # 入度表
        adjacency = [[] for _ in range(numCourses)]     # 邻接表
        queue = []
        result = []     # 存放拓扑序列
        # 计算入度
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # 把入度为0的节点加入队列
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)

        while queue:
            pre = queue.pop(0)
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
            result.append(pre)
        # 拓扑顺序列表的节点数如果是和图的节点数相同，该拓扑顺序表是该图其中一种拓扑序列。
        return result if len(result) == numCourses else []
```


### 3. 课程表III
https://leetcode-cn.com/problems/course-schedule-iii/

待续……
