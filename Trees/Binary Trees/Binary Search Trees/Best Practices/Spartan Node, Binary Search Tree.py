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
                    if current.left is None:
                        current.left = Node(val)
                        self.size += 1
                        return
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(val)
                        self.size += 1
                        return
                    else:
                        current = current.right

    def delete(self, val):
        del_parent, del_child_dir, del_target = self._get_target_anc_dtls(val)
        # Value for deletion not present
        if del_target is None:
            return
        # is root
        if self.root.data == del_target.data:
            self._splice(self.root, del_child_dir, del_target, val)
        else:
            self._splice(del_parent, del_child_dir, del_target, val)

    def _splice(self, del_parent, del_child_dir, del_target, val):
        # if target is leaf; delete target from parent
        if del_target.is_leaf():
            self._update_del_parent(del_child_dir, del_parent, None)

        # if target has no left child; shift target's right child up
        elif del_target.has_left is False:
            self._update_del_parent(
                del_child_dir, del_parent, del_target.right)

        # if target has no right child; shift target's left side up
        elif del_target.has_right is False:
            self._update_del_parent(del_child_dir, del_parent, del_target.left)

        # Both children present; find next highest value that is less than
        # target.data and substitute the value
        else:
            # Next highest value will not have a left child
            subst_parent, substitute = self._get_next_highest_below(del_target)
            del_target.data = substitute.data
            del_target.left = substitute.left
            # subst_parent.right = None

            # Update parent of node used for substitution
            # Because get_next_highest always returns the left for
            # substitution the second substitution will always be on
            # subst_parent's left
            # subst_parent.left = substitute.right
            self.size -= 1

    def _update_del_parent(self, del_child_dir, del_parent, new_val):
        # direction of `None` designates root value
        if new_val is not None:
        	new_val = new_val.data
        if del_child_dir is None:
            self.root = new_val
        elif del_child_dir == 'left':
            del_parent.left = new_val
        else:				# 'right'
            del_parent.right = new_val
        self.size -= 1

    def _get_next_highest_below(self, target):
        current = target
        parent, current = current, current.left
        # Descend to furthest right node; highest value less than target
        while current.has_right():
            parent, current = current, current.right

        return parent, current

    def _get_target_anc_dtls(self, val):
        if self.root.data == val:
            return None, None, self.root
        else:
            current = self.root
            parent = None
            dirn = None
            while True:
                if val == current.data:
                    return parent, dirn, current
                elif val < current.data:
                    if current.left is None:
                        return None, None, None
                    else:
                        parent, dirn, current = current, 'left', current.left
                        dirn = 'left'
                else:  # val > current.data
                    if current.right is None:
                        return None, None, None
                    else:
                        parent, dirn, current = current, 'right', current.right

    # Iterative function for inorder tree traversal
    def inOrder(self):

        # Set current to root of binary tree
        current = self.root
        s = []  # initialze stack
        done = 0

        while(not done):

            # Reach the left most Node of the current Node
            if current is not None:

                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                s.append(current)

                current = current.left

            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            else:
                if(len(s) > 0):
                    current = s.pop()
                    print current.data,

                    # We have visited the node and its left
                    # subtree. Now, it's right subtree's turn
                    current = current.right

                else:
                    done = 1

	# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


class Node:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

    def is_leaf(self):
        if self.right is None and self.left is None:
            return True
        else:
            return False

    def has_children(self):
        if self.right is not None and self.left is not None:
            return True
        else:
            return False

    def has_left(self):
        if self.left is not None:
            return True
        else:
            return False

    def has_right(self):
        if self.right is not None:
            return True
        else:
            return False

    # def is_val(self, val):


t = BinarySearchTree()
t.insert(5)
t.insert(11)
t.insert(4)
t.insert(35)
t.insert(3)
t.insert(5)
t.insert(19)
t.insert(-2)
t.insert(0)
t.insert(7)
t.insert(9)
t.insert(3)
t.insert(2)
t.insert(1)
t.insert(6)
t.insert(8)
t.insert(12)
print t.root.data
print t.size
print t.root.right.data
print t.root.right.right.data
parent, direction, target = t._get_target_anc_dtls(8)
print parent.data
print direction
print target.data
print target.left
print target.right
print t.inOrder()
t.delete(8)
print t.inOrder()
print t.root.data
print t.root.left.data
print t.root.right.data
t.delete(3)
print t.inOrder()
t.delete(5)
print t.root.data
print t.root.left.data
print t.root.right.data
print t.inOrder()
parent, direction, target = t._get_target_anc_dtls(8)
print parent
print target
parent, direction, target = t._get_target_anc_dtls(7)
print parent.data
print direction
print target.data
subst_parent, subst = t._get_next_highest_below(target)
print subst_parent.data
print subst.data
