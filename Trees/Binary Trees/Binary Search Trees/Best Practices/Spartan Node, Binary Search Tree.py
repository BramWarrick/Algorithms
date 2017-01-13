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

    def delete(self, val):
        parent, child_direction, target = get_parent_and_target(val)
        # is root
        if parent is None:
            # TODO
            pass
        # if target is leaf; delete target from parent
        if target.is_leaf:
            if child_direction == 'left':
                parent.leftChild = None
            else:				# 'right'
                parent.rightChild = None
        # if target has no left child; shift target's right child up
        elif target.has_leftChild is False:
            if child_direction == 'left':
                parent.leftChild = target.rightChild
            else:				# 'right'
                parent.rightChild = target.rightChild
        # if target has no right child; shift target's left side up
        elif target.has_rightChild is False:
            if child_direction == 'left':
                parent.leftChild = target.leftChild
            else:				# 'right'
                parent.rightChild = target.leftChild
        # if both children present; find next lowest value & substitute
        else:
        	# TODO Handle if substitute has right child
            sub_parent, substitute = get_next_highest(target)
            if child_direction == 'left':
                parent.leftChild.data = substitute.data
                sub_parent.leftChild = None
            else:				# 'right'
                parent.rightChild.data = substitute.data
                sub_parent.leftChild = None
        # 	Next lowest value will be a leaf, logically
        pass

    def get_next_highest(self, target):
        current = target
        while current.has_leftChild:
            parent = current
            current = current.leftChild
        return parent, current

    def get_parent_and_target(self, val):
        if self.root.data == val:
            return None, self.root
        else:
            current = self.root
            parent = None
            while True:
                if val == current.data:
                    return parent, current
                elif val < current.data:
                    if current.leftChild is None:
                        return parent, '<', current
                    else:
                        parent = current
                        current = current.leftChild
                else:
                    if current.rightChild is None:
                        return parent, '>', current
                    else:
                        parent = current
                        current = current.rightChild


class Node:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.leftChild = left
        self.rightChild = right

    def is_leaf(self, node):
        if node.rightChild is not None or node.leftChild is not None:
            return False
        else:
            return True

    def has_children(self, node):
        if node.rightChild is not None and node.leftChild is not None:
            return True
        else:
            return False

    def has_leftChild(self, node):
        if node.leftChild is not None:
            return True
        else:
            return False

    def has_rightChild(self, node):
        if node.rightChild is not None:
            return True
        else:
            return False


t = BinarySearchTree()
t.insert(4)
t.insert(5)
print t.root.data  # this works
print t.size
print t.root.rightChild.data
# print t.root.rchild.data #this works too
