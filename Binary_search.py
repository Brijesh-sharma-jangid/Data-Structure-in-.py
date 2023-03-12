def binary_search(arr, elt, left, right):
    if left > right:
        return None
    else:
        mid = (left + right) // 2
        if arr[mid] == elt:
            return mid
        elif arr[mid] < elt:
            return binary_search(arr, elt, mid + 1, right)
        else:  # lis[mid] > elt
            return binary_search(arr, elt, left, mid - 1)


if __name__ == '__main__':
    lis = [0, 1, 2, 3, 4]
    temp = binary_search(lis, 5, 0, len(lis) - 1)
    print(temp)
