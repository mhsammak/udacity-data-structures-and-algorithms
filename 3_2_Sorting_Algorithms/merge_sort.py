def _merge(array: list, left: int, mid: int, right: int) -> None:
    size = right - left + 1
    temp = [None for _ in range(size)]

    first = left
    second = mid + 1
    for i in range(size):
        if first > mid:
            temp[i] = array[second]
            second += 1
        elif second > right:
            temp[i] = array[first]
            first += 1
        elif array[first] > array[second]:
            temp[i] = array[second]
            second += 1
        else:
            temp[i] = array[first]
            first += 1

    for i in range(size):
        array[left+i] = temp[i]


def _merge_sort(array: list, left: int, right: int):
    size = right - left + 1
    if size <= 1:
        return
    else:
        mid = (right + left) // 2
        _merge_sort(array, left, mid)
        _merge_sort(array, mid+1, right)
        _merge(array, left, mid, right)


def sort(array: list) -> None:
    """
    Sorts the array in ascending order.

    Args:
        array (list): array of elements
    Returns:
        None
    """
    _merge_sort(array, 0, len(array)-1)



if __name__ == '__main__':
    array1 = [2, 13, 1, 14, 6]
    array2 = []
    array3 = [112, 13]

    sort(array1)
    sort(array2)
    sort(array3)

    print(' '.join([str(i) for i in array1]))
    print(' '.join([str(i) for i in array2]))
    print(' '.join([str(i) for i in array3]))
