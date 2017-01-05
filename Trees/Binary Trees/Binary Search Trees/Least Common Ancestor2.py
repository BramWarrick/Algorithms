def question4(T, r, n1, n2):
    if question4_validations(T, r, n1, n2) == False:
        return None
    if n1 > n2:
        low, high = n2, n1
    else:
        low, high = n1, n2
    # r != n1 or n2, set to current_val
    current_val = r
    child_left, child_right = question4_return_children(T, current_val)

if not child_left and not child_right:
	return None
if low < current_val and current_val < high:
	return current_val
if low == current_val or high == current_val:
	return previous_val
if high > current_val or child_right is None:
	previous_val = current_val
	current_val = child_left
	child_left, child_right = question4_return_children(T, current_val)
if low > current_val or child_left is None:
	previous_val = current_val
	current_val = child_left
	child_left, child_right = question4_return_children(T, current_val)


    while child_left is not None and child_right is not None:
        if child_left is None and (current_val < n1 and current_val < n2):
            previous_val = current_val
            current_val = child_right
            child_left, child_right = question4_return_children(T, current_val)
        if child_right is None and (current_val > n1 and current_val > n2):
            previous_val = current_val
            current_val = child_left
            child_left, child_right = question4_return_children(T, current_val)
        if child_left == n1 or child_left == n2 or child_right == n1 or child_right == n2:
            print 'yes'
            return previous_val
        if child_left < current_val < child_right:
            return current_val
    return None


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

# print "Question 4 Tests"
# print question4([[0, 1, 0, 0, 0],
#                  [0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0],
#                  [1, 0, 0, 0, 1],
#                  [0, 0, 0, 0, 0]],
#                 3,
#                 1,
#                 4)
# print "Expected output: 3"
# print question4([],
#                 0,
#                 1,
#                 4)
# print "Expected output: None"
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
# print question4([[0, 0, 0, 0, 0, 0, 0],
#                  [1, 0, 1, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [0, 1, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 1, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 1]],
#                 5,
#                 2,
#                 0)
# print "Expected output: 1"
# print question4([[0, 0, 1, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [0, 1, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [1, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 1, 0, 1],
#                  [0, 0, 0, 1, 0, 0, 0]],
#                 5,
#                 1,
#                 2)
# print "Expected output: 0"
# print question4([[0, 0, 0, 0, 0, 0, 0],
#                  [1, 0, 1, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [0, 1, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 1, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 1]],
#                 5,
#                 5,
#                 0)
# print "Expected output: None"
# print question4([[0, 0, 1, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [0, 1, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [1, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 1, 0, 1],
#                  [0, 0, 0, 1, 0, 0, 0]],
#                 None,
#                 1,
#                 2)
# print "Expected output: None"
# print question4([[0, 0, 1, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [0, 1, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [1, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 1, 0, 1],
#                  [0, 0, 0, 1, 0, 0, 0]],
#                 5,
#                 None,
#                 2)
# print "Expected output: None"
# print question4([[0, 0, 1, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [0, 1, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0],
#                  [1, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 1, 0, 1],
#                  [0, 0, 0, 1, 0, 0, 0]],
#                 5,
#                 1,
#                 None)
# print "Expected output: None"
