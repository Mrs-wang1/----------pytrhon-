def quick_sort(alist,first,last):
    """快速排序"""
    if first >= last:
        return
    # n = len(alist)
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
                high -= 1
        alist[low] = alist[high]
        #low += 1
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        #high -= 1
    #从循环退出时，low == high
    alist[low] = mid_value
    #对low左边的列表执行快速排序
    quick_sort(alist,first,low-1)
    #对low右边的列表排序
    quick_sort(alist,low+1,last)

def quick_sort2(list):
    """快速排序"""
    #此处为递归调用的终止条件，即列表长度为1时，函数停止运行
    if len(list) < 2:
        return list
    else:
        mid_value = list[0]
        less = [i for i in list[1:] if i <= mid_value]
        greater = [i for i in list[1:] if i > mid_value]
        return quick_sort2(less) + [mid_value] + quick_sort2(greater)

if __name__ == "__main__":
    li = [11, 33, 23, 43, 47, 58, 97, 61]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)
    list = [13,23,25,32,37,48,54,67,79,83,97]
    print(list)
    quick_sort2(list)