import sys
sys.setrecursionlimit(10**6)


def ffs(adj, vis, i):
    vis[i] = 1
    for it in adj[i]:
        if vis[it] == 0:
            ffs(adj, vis, i)


def dfs(adj, vis, i, vc):
    vis[i] = 1
    for it in adj[i]:
        if vis[it] == 0:
            dfs(adj, vis, i, vc)
    vc.append(i)


def number_of_strongly_connected_components(adj):
    result = 0
    vis = [0] * len(adj)
    vc = []
    for i in range(len(adj)):
        if vis[i] == 0:
            dfs(adj, vis, i, vc)
    mat = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            mat[adj[i][j]].append(i)
    vis = [0] * len(mat)
    for i in vc:
        if vis[i] == 0:
            ffs(mat, vis, i)
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
