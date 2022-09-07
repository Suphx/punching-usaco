"""
题目链接：
http://www.usaco.org/index.php?page=viewproblem2&cpid=1230&lang=zh

Test Input:
4
2 10
3 20
4 30
1 40

Test Output:
90
"""

import sys  # 导入sys模块
sys.setrecursionlimit(100000)

a, v = [], []  # cow i 访问 cow a[i] 并且会叫 v[i] 声
graph = []  # graph[i] 存储 cow i 会前往 farm i
visited = []  # 标记 farm i 是否已经被访问


def mark(y):
    """

    :param y:
    :return:
    """
    # if visited[y]:
    #     return
    # visited[y] = True
    # for c in graph[y]:
    #     mark(c)

    stack = [y]
    visited[y] = True
    while stack:
        tmp = stack.pop()
        for c in graph[tmp]:
            if not visited[c]:
                stack.append(c)
                visited[c] = True
    return


def min_in_cycle(curr):
    y = a[curr]
    z = a[y]
    while y != z:
        y = a[y]
        z = a[a[z]]

    # y is now an element that is in the cycle
    min_v = v[y]
    y = a[y]

    # traverse the cycle to find the cow with the minimum v_i value
    while y != z:
        min_v = min(min_v, v[y])
        y = a[y]

    mark(y)
    return min_v


if __name__ == '__main__':
    # f = open("prob1_silver_open22/2.in", encoding="utf-8")
    n = int(input())

    a, v = [], []  # cow i 访问 cow a[i] 并且会叫 v[i] 声
    graph = [[] for _ in range(n)]  # graph[i] 存储 cow i 会前往 farm i
    visited = [False for _ in range(n)]  # 标记 farm i 是否已经被访问

    max_moos = 0
    for i in range(n):
        ai, vi = [int(i) for i in input().split(" ")]
        a.append(ai)
        v.append(vi)

        a[i] -= 1
        graph[a[i]].append(i)
        max_moos += v[i]

    for i in range(n):
        if not visited[i]:
            max_moos -= min_in_cycle(i)

    # out = open("prob1_silver_open22/2.out")
    # ans = int(out.readline())
    # assert max_moos == ans

    print(max_moos)


