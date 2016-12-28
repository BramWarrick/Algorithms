# A Dynamic Programming based Python program for LPS problem
# Returns the length of the longest palindromic subsequence in seq


def LPSubsequence(a):
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
                L[start][stop] = LPSubsequenceHelper(
                    L[start][stop - 1], L[start + 1][stop])

    return L[0][sl - 1]


def LPSubsequenceHelper(string1, string2):
    if len(string1) >= len(string2):
        return string1
    else:
        return string2

print LPSubsequence('dd')
print LPSubsequence('dald')

