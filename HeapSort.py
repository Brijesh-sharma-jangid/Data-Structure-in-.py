def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1

def bubble_down(arr, i, n):
    if left(i) > n:
        return
    if left(i) <= len(arr) < n:
        if arr[i] > arr[left(i)]:
            arr[i], arr[left(i)] = arr[left(i)], arr[i]
            bubble_down(arr,left(i),n)
    else:
        min_child_value, min_child_index = min((arr[left(i)], left(i)), (arr[right(i)], right(i)))
        arr[i], arr[min_child_index] = arr[min_child_index], arr[i]
        bubble_down(arr,min_child_index,n)
    return

if __name__ == '__main__':
    lis = [None,5,2,4,-1,7]
    n = len(lis)-1
    for i in range(n, 0, -1):
        bubble_down(lis, i, n)
    print(lis[1:])
