class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.size += 1
        else:
            current = self.root
            while True:
                if val == current.data:
                    return
                elif val < current.data:
                    if current.lefchild is None:
                        current.leftChild = Node(val)
                        self.size += 1
                        return
                    else:
                        current = current.leftChild
                else:
                    if current.rightChild is None:
                        current.rightChild = Node(val)
                        self.size += 1
                        return
                    else:
                        current = current.rightChild

class Node:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.leftChild = left
        self.rightChild = right


t = BinarySearchTree()
t.insert(4)
t.insert(5)
print t.root.data #this works
print t.size
print t.root.rightChild.data
# print t.root.rchild.data #this works too
