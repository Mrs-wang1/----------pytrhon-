class Deque(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_front(self,item):
        self.__list.insert(0,item)

    def add_rear(self,item):
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)

    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    q = Deque()
    q.add_front(1)
    q.add_front(2)
    q.add_front(3)
    q.add_front(4)
    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_front())
    q.add_rear(4)
    q.add_rear(3)
    q.add_rear(2)
    q.add_rear(1)
    print(q.pop_rear())
    print(q.pop_rear())
    print(q.pop_rear())
    print(q.pop_rear())