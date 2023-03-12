def copy_back(output_lst, lst, left, right):
    assert (len(output_lst)  ==  right - left + 1)
    for i in range(left, right + 1):
        lst[i] = output_lst[i - left]
    return

def marge(arr, left, mid, right):
    i = left
    j = mid + 1
    temp = []
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i = i + 1
        else:
            temp.append(arr[j])
            j = j + 1
    while i <= mid:
        temp.append(arr[i])
        i = i + 1
    while j <= right:
        temp.append(arr[j])
        j = j + 1
    copy_back(temp, arr, left, right)


def marge_sort(lis, left, right):
    if left < right:
        mid = (left + right) // 2
        marge_sort(lis, left, mid)
        marge_sort(lis, mid + 1, right)
        marge(lis, left, mid, right)


if __name__ == '__main__':
    arr = [10, 4, 7, 6, 0]
    marge_sort(arr, 0, len(arr) - 1)
    for i in arr:
        print(i, end=" ")
