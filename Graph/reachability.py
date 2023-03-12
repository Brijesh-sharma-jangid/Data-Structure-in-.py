import sys

def dfs(adj, vis, i, chek, sum):
    vis[i] = 1
    chek[i] = sum
    for it in adj[i]:
        if vis[it] != 1:
            dfs(adj, vis, it, chek, sum)


def reach(adj, x, y):
    vis = [0] * len(adj)
    chek = [0] * len(adj)
    sum = 1
    for i in range(len(adj)):
        if vis[i] == 0:
            dfs(adj, vis, i, chek, sum)
            sum = sum + 1
    if chek[x] != chek[y]:
        return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))