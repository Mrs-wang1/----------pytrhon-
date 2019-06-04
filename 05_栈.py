class stack(object):
    """栈"""
    def __init__(self):
        #私有属性
        self.__list = []

    def push(self,item):
        """压入元素"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if  self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty( ):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())