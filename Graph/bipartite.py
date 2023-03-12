import sys
from queue import Queue

def bipartite(adj):
    bip = [-1] * len(adj)
    q = Queue()
    q.put(0)
    bip[0] = 1
    while not q.empty():
        node = q.get()
        for i in adj[node]:
            if bip[i] == -1:
                bip[i] = 1 - bip[node]
                q.put(i)
            elif bip[i] == bip[node]:
                return 0
    return 1

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
    print(bipartite(adj))
