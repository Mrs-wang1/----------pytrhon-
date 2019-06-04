#coding:utf-8
def shell_sort(alist):
     """希尔排序"""
     n = len(alist)
     gap = n // 2
     #gap变化到0之前，插入算法执行的次数
     while gap >0:
         #与插入算法相比，区别就是gap步长
         for i in range(gap,n):
             # i = [gap,gap+1,gap+2....n-1]
             j = i
             while j > 0:
                 if alist[j] < alist[j-gap]:
                    alist[j],alist[j-gap] = alist[j-gap],alist[j]
                    j -= gap
                 else:
                    break
         #缩短步长
         gap //= 2



if __name__ == "__main__":
    li = [11,33,23,43,47,58,97,61]
    print(li)
    shell_sort(li)
    print(li)