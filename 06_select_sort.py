def select_sort(alist):
    """选择排序
    一次选择列表中的最小值
    然后放在最前面
    即列表最前面为有序列表，后面为无序序列
    """
    n = len(alist)
    for j in range(0,n-1):#j:1,2,3,4...n-2
        min_index = j
        for i in range(j+ 1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]



if __name__ == "__main__":
    list = [54,26,32,16,57,87,90,20]
    print(list)
    select_sort(list)
    print(list)
