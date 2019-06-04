def merge_sort(list):
    """归并排序"""
    n = len(list)
    #递归调用停止条件
    if n < 2:
        return list
    mid = n // 2
    # left代表采用归并排序返回的序列，right亦同
    left_li = merge_sort(list[:mid])
    right_li = merge_sort(list[mid:])

    left_pointer,right_pointer = 0,0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer +=1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    li = [11, 33, 23, 43, 47, 58, 97, 61]
    print(li)
    sorted_li = merge_sort(li)
    print(li)
    print(sorted_li)