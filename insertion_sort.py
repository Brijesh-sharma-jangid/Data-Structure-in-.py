def insert(A, j):
    for i in range(j - 1, -1, -1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]  # swap
        else:
            break


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(0, n):
        k = int(input())
        arr.append(k)
    for i in range(0, len(arr)):
        insert(arr, i)
    for i in arr:
        print(i,end=" ")

