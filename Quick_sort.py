def Partition(Arr, left, right) -> int:
    i = left - 1
    j = left
    x = Arr[right]
    while j < right:
        if Arr[j] <= x:
            i = i + 1
            Arr[i], Arr[j] = Arr[j], Arr[i]
            j = j + 1
        else:
            j = j + 1
    Arr[i + 1], Arr[right] = Arr[right], Arr[i + 1]
    return i + 1


def Quick_sort(Arr, left, right):
    if left < right:
        pivot = Partition(Arr, left, right)
        Quick_sort(Arr, left, pivot - 1)
        Quick_sort(Arr, pivot + 1, right)


if __name__ == '__main__':
    Arr = [10, 5, 8, 6, 5]
    Quick_sort(Arr, 0, len(Arr) - 1)
    print(Arr[0:])
