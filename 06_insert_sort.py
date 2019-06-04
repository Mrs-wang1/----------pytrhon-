def insert_sort(alist):
    """插入排序
    把后面数字插入前面有序列中的正确位置
    """
    n = len(alist)
    # 从右边的无序序列中读取多少个元素执行这样的过程
    for j in range(1,n):
        #J = [1,2,3,...n-1]
        # i 代表内层循环的起始值
        i = j
        #执行从右边的无序序列中取出的第一个元素，即i位置元素，然后将其插入到前面的正确位置中
        while i > 0:
             if alist[i] < alist[i-1]:
                alist[i] ,alist[i-1] = alist[i-1],alist[i]
                i -= 1
             else:
                break

if __name__ == "__main__":
    list = [54,26,32,16,57,87,90,20]
    print(list)
    insert_sort(list)
    print(list)


