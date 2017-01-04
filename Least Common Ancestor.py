# Question 4  - Udacity specs
# Find the least common ancestor between two nodes on a binary search
# tree. The least common ancestor is the farthest node from the root that
# is an ancestor of both nodes. For example, the root is a common ancestor
# of all nodes on the tree, but if both nodes are descendents of the
# root's left child, then that left child might be the lowest common
# ancestor. You can assume that both nodes are in the tree, and the tree
# itself adheres to all BST properties. The function definition should
# look like question4(T, r, n1, n2), where T is the tree represented as a
# matrix, where the index of the list is equal to the integer stored in
# that node and a 1 represents a child node, r is a non-negative integer
# representing the root, and n1 and n2 are non-negative integers
# representing the two nodes in no particular order. For example, one test
# case might be


class BSTNode(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree(object):
    def __init__(self, value):
        self.root = BSTNode(value)


def question4(T, r, n1, n2):
    # Validations
    if r is None or n1 is None or n2 is None:
        return None
    if T is None or T == []:
        return None
    # Create root node on binary search tree, then use function to complete it
    tree = BinarySearchTree(r)
    tree = question4_build_tree(T, tree.root, tree)
    # Return the least common ancestor
    return question4_find_lca(tree, n1, n2)


def question4_build_tree(T, node, tree):
    """Recursive - Takes table T and initialized tree and creates all other nodes

    node is required due to recursive calls.
    """
    r = node.value
    # Radiating from root, progressively add nodes as looked up from T
    # This approach allows it to skip values that aren't a part of the tree
    # and builds the tree top-down as expected.
    # No base case because the number of nodes limits the recursive calls
    for index in xrange(0, len(T[r])):
        if T[r][index] == 1:
            if index < r:
                node.left = BSTNode(index)
                question4_build_tree(T, node.left, tree)
            else:
                node.right = BSTNode(index)
                question4_build_tree(T, node.right, tree)
    return tree


def question4_find_lca(tree, n1, n2):
    # Find each target node on the tree and return ancestor list
    # node variables are artifacts of recursive calls, can be disregarded
    node1, ancestors1 = question4_find_node(tree, tree.root, n1, [])
    node2, ancestors2 = question4_find_node(tree, tree.root, n2, [])
    # Tidyness: set `la' variables to length of ancestor lists, respectively
    la1, la2 = len(ancestors1), len(ancestors2)
    for node1 in xrange(1, la1 + 1):
        for node2 in xrange(1, la2 + 1):
            if ancestors1[la1 - node1] == ancestors2[la2 - node2]:
                return ancestors1[len(ancestors1) - node1]


def question4_find_node(tree, node, find_val, ancestors):
    """ Recursive - Returns node and the nodes ancestors

    Arguments:
    tree - binary search tree
    node - binary search node
    find_val - value of node to be found
    ancestors - list of nodes passed through on way to target node

    Returns tuple:
    node as a node
    ancestors as a list
    """
    if node is None:            # First base case
        return
    if node.value == find_val:  # Second base case
        return node, ancestors
    elif node.value > find_val:
        ancestors.append(node.value)
        return question4_find_node(tree, node.left, find_val, ancestors)
    else:
        ancestors.append(node.value)
        return question4_find_node(tree, node.right, find_val, ancestors)


print "Question 4 Tests"
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                1,
                4)
print "Expected outputs: 3"
print question4([],
                0,
                1,
                4)
print "Expected outputs: None"
print question4([[0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],
                3,
                1,
                2)
print "Expected output: 0"
print question4([[0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],
                3,
                5,
                6)
print "Expected output: 3"
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1]],
                5,
                2,
                0)
print "Expected output: 1"
print question4([[0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0]],
                5,
                1,
                2)
print "Expected output: 0"
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1]],
                5,
                5,
                0)
print "Expected output: None"
print question4([[0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0]],
                None,
                1,
                2)
print "Expected output: None"
print question4([[0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0]],
                5,
                None,
                2)
print "Expected output: None"
print question4([[0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0]],
                5,
                1,
                None)
print "Expected output: None"

# Question 4 Commentary - O(nlogn)

# Efficiency:
# - Overall: O(n * m) + O(logn) - first for tree build, second for search/lca
# - Build tree: O(n * m) - where n is the number of nodes and m is the width
# of the matrix. This is because each node must be visited and then must be
# evaluated for children across the width of the matrix (creating the m).
# - Search tree: O(2logn), simplifying to O(logn) - where `n` is the number
# of nodes. Binary search for two nodes, standard reasoning applies.
# - Finding ancestor: O(2logn), simplifying to O(logn) - where `n` is the number
# of nodes. In this case it's the result of evaluating across the ancestor
# list for each searched node.

# Efficiency Design:
# - I only visit nodes that are present as I build the tree and make no
# comparisons that are not essential.
# - The search follows classic binary search tree patterns and so it takes a
# very direct O(logn) approach that cannot be improved upon within this
# datastructure.
# - The ancestor lists that are returned are never longer than log(n), so 
# typically short and generally require few evaluations. This seemed both the
# fastest and least memory intensive solution.

# Process:
# Since the root is provided, I start traversing the tree at that entry. As
# new nodes are found (designated by the boolean `1`), I jump to the next
# node and treat it the same - iteratively.

# With the tree built, I find each of the target nodes, building an `ancestor`
# list for each. After these lists are returned, I loop through them, starting
# at the back, until a shared ancestor is found. I work backwards on one list,
# then the second - which you can see with the nested `for` loop.

# Addt'l Note:
# I took the definition of 'ancestor' literally, so any search for the root
# value will result in `None`. No value can be its own ancestor (e.g. searching
# for a parent and child, will return the parent's parent).