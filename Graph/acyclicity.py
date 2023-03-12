#Uses python3
import sys

def dfs(adj, vis, i, temp):
    vis[i] = 1
    temp[i] = 1
    for it in adj[i]:
        if vis[it] == 0:
            if dfs(adj,vis,it,temp) == 1:
                return 1
        elif temp[it] == 1:
            return 1
    temp[i] = 0
    return 0

def acyclic(adj):
    vis = [0]*len(adj)
    temp = [0]*len(adj)
    ans = 0
    for i in range(len(adj)):
        if vis[i] == 0:
            if dfs(adj,vis,i,temp) == 1:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
