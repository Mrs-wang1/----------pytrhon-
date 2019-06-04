def  buble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        #优化有序序列的排序时间
        count = 0
        for i in range(0,n-1-j):
             if alist[i] > alist[i+1]:
                 alist[i],alist[i+1] = alist[i+1],alist[i]
                 count += 1
        #即序列为有序序列时，不发生次序交换
        if count == 0:
            return


if __name__ == "__main__":
    list =[3,1,4,7,5,9,10,6]
    print(list)
    buble_sort(list)
    print(list)