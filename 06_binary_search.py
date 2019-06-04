def binary_search(list,item):
    """二分查找,递归"""
    # first = 0
    # last = len(list) - 1
    n = len(list)
    if n > 0:
        mid = n // 2
        if list[mid] == item:
            return True
        elif item < list[mid]:
            return binary_search(list[:mid],item)
        else:
            return binary_search(list[mid+1:],item)
    return False


def binary_search_1(list,item):
    """二分查找，非递归"""
    n = len(list)
    first = 0
    last = n -1
    while first <= last:
        mid = (first + last) // 2
        if list[mid] == item:
            return True
        elif item < list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False




if __name__ == "__main__":
    li = [2,4,5,6,7,8,10,12]
    print(binary_search(li, 2))
    print(binary_search(li, 0))
    print(binary_search_1(li,2))
    print(binary_search_1(li,0))