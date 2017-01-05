def question4(T, r, n1, n2):
    if question4_validations(T, r, n1, n2) == False:
        return None
    if n1 > n2:
        low, high = n2, n1
    else:
        low, high = n1, n2
    # r != n1 or n2, set current_val and initialize previous_val to `r`
    current_val = r
    previous_val = r
    child_left, child_right = question4_return_children(T, current_val)
    while True:
        # print "current_val, child_left, child_right = " + str(current_val) + ", " + str(child_left) + ", " + str(child_right)
        # print "low, high = " + str(low) + ", " + str(high)
        if child_left is None and child_right is None:
            # One or more of the nodes don't exist in the tree; fail
            return None
        if low < current_val and current_val < high:
            # current node is branching point for targeted nodes
            return current_val
        if low == current_val or high == current_val:
            # Current node is one of the requested nodes; return previous node
            return previous_val
        if high < current_val:
            # high is less than current node or right branch doesn't exist
            # Continue down left side
            previous_val = current_val
            current_val = child_left
            child_left, child_right = question4_return_children(T, current_val)
        if low > current_val:
            # print "low > current_val or child_left is None"
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
