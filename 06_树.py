class Node(object):

    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):

    def __init__(self):
        self.root = None
    #添加元素
    def add(self,item):
        node = Node(item)
        #判断根节点是否为空
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_trave(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    #先序遍历的顺序为：根、左、右
    def  preoder(self,node):
        """先序遍历"""
        if node is None:
            return
        print(node.elem,end=" ")
        self.preoder(node.lchild)
        self.preoder(node.rchild)
    #中序遍历顺序为：左、根、右
    def inoder(self,node):
        """中序遍历"""
        if node is None:
            return
        self.inoder(node.lchild)
        print(node.elem, end=" ")
        self.inoder(node.rchild)


    def postoder(self,node):
        """后序遍历"""
        if node is None:
            return
        self.postoder(node.lchild)
        self.postoder(node.rchild)
        print(node.elem, end=" ")




if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_trave()
    print(" ")
    tree.preoder(tree.root)
    print(" ")
    tree.inoder(tree.root)
    print(" ")
    tree.postoder(tree.root)