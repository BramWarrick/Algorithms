class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.leftChild = left
        self.rightChild = right
