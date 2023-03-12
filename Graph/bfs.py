#Uses python3
import sys
from queue import Queue

def distance(adj, s, t):
    dist = [sys.maxsize] * len(adj)
    dist[s] = 0
    q = Queue()
    q.put(s)
    while not q.empty():
        node = q.get()
        for i in adj[node]:
            if dist[node] + 1 < dist[i]:
                dist[i] = dist[node] + 1
                q.put(i)
    if dist[t] == sys.maxsize:
        return -1
    return dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
