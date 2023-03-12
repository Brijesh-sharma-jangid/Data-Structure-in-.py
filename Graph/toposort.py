#Uses python3

import sys
from queue import LifoQueue


def dfs(adj, used, stack, x):
    used[x] = 1
    for it in adj[x]:
        if used[it] == 0:
            dfs(adj, used, stack, it)
    stack.put(x)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    stack = LifoQueue()
    for i in range(len(adj)):
        if used[i] == 0:
            dfs(adj, used, stack, i)
    while not stack.empty():
        order.append(stack.get())
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

