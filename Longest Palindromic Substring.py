# A Dynamic Programming based Python program for LPS problem
# Returns the length of the longest palindromic subsequence in seq


def question2(a):
    sl = len(a)     # sl is string length

    # Create a table to store results of subproblems
    L = [[0 for x in range(sl)] for x in range(sl)]

    # Create palindrome of 1 for each character in input string (a)
    for i in range(sl):
        L[i][i] = a[i]

    # Build the table. Note that the starter diagonal values of table are
    # useless and not filled in the process. The values are filled in a
    # manner similar to Matrix Chain Multiplication DP solution (See
    # http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    # cl is check string length
    for cl in range(2, sl + 1):
        for start in range(sl - cl + 1):
            stop = start + cl - 1
            if a[start] == a[stop] and cl == 2:
                L[start][stop] = a[start] * 2
            elif a[start] == a[stop]:
                L[start][stop] = a[start] + L[start + 1][stop - 1] + a[stop]
            else:
                L[start][stop] = question2helper(
                    L[start][stop - 1], L[start + 1][stop])

    return L[0][sl - 1]


def question2helper(string1, string2):
    if len(string1) >= len(string2):
        return string1
    else:
        return string2

print question2('dd')
print question2('dald')


def question2a(a):
    if a is None or a == '':
        return ''

    maxPalLength = 1
    n = len(a)
    palPosStart = 0

    start = 0
    stop = 0

    for index in xrange(1, n):
        start = index - 1
        stop = index

        while start >= 0 and stop < n and a[start] == a[stop]:
            if stop - start + 1 > maxPalLength:
                palPosStart = start
                maxPalLength = stop - start + 1
            start -= 1
            stop += 1

        start = index - 1
        stop = index + 1

        while start >= 0 and stop < n and a[start] == a[stop]:
            if stop - start + 1 > maxPalLength:
                palPosStart = start
                maxPalLength = stop - start + 1
            start -= 1
            stop += 1
        print maxPalLength
    return a[palPosStart:(palPosStart + maxPalLength)]


print question2a('dasvad')
