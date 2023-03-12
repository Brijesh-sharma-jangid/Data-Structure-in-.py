#Uses python3

import sys


def negative_cycle(adj, cost):
    # bellman ford
    # relax v - 1 vertex
    # -ve cycle perform vth iteration if dist values changes then present
    dist = [sys.maxsize] * len(adj)
    dist[0] = 0
    for _ in range(0,len(adj) - 1):
        for index_i, i in enumerate(adj):
            for index_j, j in enumerate(i):
                if dist[j] > dist[index_i] + cost[index_i][index_j]:
                    dist[j] = dist[index_i] + cost[index_i][index_j]

    for index_i, i in enumerate(adj):
        for index_j, j in enumerate(i):
            if dist[j] > dist[index_i] + cost[index_i][index_j]:
                return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # n - vertex
    # m - edges
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
