def question4(T, r, n1, n2):
    if question4_validations(T, r, n1, n2) == False:
        return None
    if n1 > n2:
        low, high = n2, n1
    else:
        low, high = n1, n2
    # r != n1 and n2; set current_val and initialize previous_val to `r`
    current_val, previous_val = r, r
    child_left, child_right = question4_return_children(T, current_val)
    while True:
        if child_left is None and child_right is None:
            # One or more of the nodes don't exist in the tree; end of branch
            return None
        if low < current_val and current_val < high:
            # Current node is branching point for targeted nodes; LCA
            return current_val
        if low == current_val or high == current_val:
            # Current node is one of the requested nodes; previous node is LCA
            return previous_val
        if high < current_val:
            # `high` is less than current node; follow left branch
            previous_val = current_val
            current_val = child_left
            child_left, child_right = question4_return_children(T, current_val)
        if low > current_val:
            # `low` is greater than current node; follow right branch
            previous_val = current_val
            current_val = child_right
            child_left, child_right = question4_return_children(T, current_val)


def question4_validations(T, r, n1, n2):
    if T is None or T == []:
        return False
    if n1 is None or n2 is None:
        return False
    if r is None or r == n1 or r == n2:
        return False
    if r < 0 or n1 < 0 or n2 < 0:
        return False
    return True


def question4_return_children(T, value):
    child_left = None
    child_right = None
    for index in xrange(0, len(T[value])):
        if T[value][index] == 1:
            if index < value:
                child_left = index
            else:
                child_right = index
    return child_left, child_right


print "Question 4 Tests"
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                1,
                4)
print "Expected output: 3"
print question4([],
                0,
                1,
                4)
print "Expected output: None"
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
# O(log(n))

# Efficiency Design:
# Throughout the process, nodes are only visited in order to return their value
# or traversed on the way to the next node for evaluation. Results are returned
# immediately and without recursion.


# Memory
# O(1)
# - I created a few variables that remain constant in their memory utilization
# across the run of the algorithm and any size of tree. 
# - I could remove `low` and `high` but I added those for improved readability.
# This could be accompished with a `n1`, `n2`swap where `n1` would be forced
# to be `low` and `n2` as `high`.

# Process:
# - I start with the root and progressively target descendants based on 
# greater/less than evaluations. Once I find:
#     - Lowest node value is less than current node & highest is greater
#     - Current node value equals the low or high node's value; return previous
# If that condition is never met, eventually the helper function will return 
# None, None and the core function will return None due to an end of 
# branch/tree. This means one of the nodes was not in the tree.
# With the tree built, I find each of the target nodes, building an `ancestor`
# list for each. After these lists are returned, I loop through them, starting
# at the back, until a shared ancestor is found. I work backwards on one list,
# then the second - which you can see with the nested `for` loop.

# Addt'l Note:
# I took the definition of 'ancestor' literally, so any search for the root
# value will result in `None`. No value can be its own ancestor (i.e. searching
# for a parent and child, will return the parent's parent).
