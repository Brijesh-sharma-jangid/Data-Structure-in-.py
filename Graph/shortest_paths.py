#Uses python3

import sys
import queue

def dfs(adj, x, sh):
    sh[x] = 0
    for i in adj[x]:
        if sh[i] == 1:
            dfs(adj, i, sh)


def shortet_paths(adj, cost, s, dist, reachable, shortest):
    dist[s] = 0
    reachable[s] = 1
    for _ in range(0,len(adj) - 1):
        for index_i, i in enumerate(adj):
            for index_j, j in enumerate(i):
                if dist[j] > dist[index_i] + cost[index_i][index_j]:
                    dist[j] = dist[index_i] + cost[index_i][index_j]
                    reachable[j] = 1

    for index_i, i in enumerate(adj):
        for index_j, j in enumerate(i):
            if dist[j] > dist[index_i] + cost[index_i][index_j]:
                dist[j] = dist[index_i] + cost[index_i][index_j]
                if shortest[j] == 1:
                    shortest[j] = 0
    for i in range(n):
        if shortest[i] == 0:
            for x in adj[i]:
                dfs(adj,x,shortest)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

