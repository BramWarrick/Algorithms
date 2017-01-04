# Question 5 - Udacity Specs
# Find the element in a singly linked list that's m elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the
# end is the 3rd element. The function definition should look like
# question5(ll, m), where ll is the first node of a linked list and m is
# the "mth number from the end". You should copy/paste the Node class
# below to use as a representation of a node in the linked list. Return
# the value of the node at that position.

def question5(ll, m):
    if ll is None:
        return None
    size = question5_get_ll_size(ll)
    if size < m or size == 0 or m is None:
        return None
    else:
        target = size - m
    # print target
    # print size
    return question5_get_target_val(ll, target)


def question5_get_ll_size(ll):
    if ll.head is None:
        return 0
    node = ll.head
    size = 1
    # Cycle through nodes gathering count
    # Last node will be skipped, but `size = 1` accommodates this for
    # accurate `size`
    while node.next is not None:
        size += 1
        node = node.next
    return size


def question5_get_target_val(ll, target):
    node = ll.head
    # Cycle through linked list, stopping at target node
    for x in range(0, target):
        node = node.next
    return node.data


class LinkedList(object):
    def __init__(self, data):
        self.head = Node(data)

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, newnext):
        self.next = newnext


print "Question 5 Tests"

ll = LinkedList(0)
ll.add(1)
ll.add(21)
ll.add(13)
print question5(ll, None)
print "Expected: None"
print question5(ll, 1)
print "Expected: 0"
print question5(ll, 2)
print "Expected: 1"
print question5(ll, 3)
print "Expected: 21"
print question5(ll, 4)
print "Expected:13"
print question5(ll, 5)
print "Expected: None"
ll.add(131)
ll.add(43)
print question5(ll, 5)
print "Expected: 131"
print question5(ll, 6)
print "Expected: 43"
ll.add(61)
print "Expected: 61"
print question5(ll, 7)
for x in xrange(1, 8):
    print question5(ll, x)
print "Expected from loop: 0 ,1, 21, 13, 131, 43, 61"
print question5(None, 1)
print "Expected: None"
print question5(None, None)
print "Expected: None"

# Question 5 Commentary

# Efficiency:
# Overall and correct answer for everything below: O(n)
# Best case: O(n) - where n is the number of nodes in list, and m is 1
# Worst case: O(2n) - where n is the number of nodes and m = n
# Generally: O(n + 2(n - m))

# Efficiency Design:
# - Because the length of the linked list is unknowable at the beginning a full
# traversal of the linked list is required in order to get the count.
# - Once the count of nodes is complete, I iterate to the (count - offset + 1)
# node and return the result.
# - Any other solution would change this from a singly linked list or could have 
# been a tremendous memory hog.

# Process:
# As a first step, I iterated through the linked list, counting the number of
# entries. Using that total, I go to the (n - m-th) node and return the result.

# Each pass was a full iteration beginning at the linked list's head.

# Addt'l Note:
# I considered tracking m number of values, but because that could use a lot of
# memory if a large list was provided with a large m, I opted for this
# solution.