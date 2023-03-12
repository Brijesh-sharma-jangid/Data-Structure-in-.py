#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    dist = [sys.maxsize] * len(adj)
    dist[s] = 0
    q = queue.PriorityQueue()
    q.put((0,s))
    while not q.empty():
        dis, node = q.get()
        for index, i in enumerate(adj[node]):
            if dist[i] > dist[node] + cost[node][index]:
                dist[i] = dist[node] + cost[node][index]
                q.put((dist[i],i))
    if dist[t] == sys.maxsize:
        return -1
    return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
