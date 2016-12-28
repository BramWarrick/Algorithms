def LPSubsequence(a):
    """
    Returns the longest palindromic subsequence within the input string

    This can be the result of dropping characters to achieve the longest palindrome
    (e.g. `abdgda` will yield a result of `adgda` because dropping the `b` allows 
    for the longest palindrome.)
    """
    if a is None or len(a) == 0:
        return ""

    sl = len(a)     # sl is string length

    # Create a table to store results of subproblems
    L = [[0 for x in range(sl)] for x in range(sl)]

    # Create palindrome of 1 for each character in input string (a)
    for i in range(sl):
        L[i][i] = a[i]

    # cl is check string length
    for cl in range(2, sl + 1):
        for start in range(sl - cl + 1):
            stop = start + cl - 1
            if a[start] == a[stop] and cl == 2:
                L[start][stop] = a[start] * 2
            elif a[start] == a[stop]:
                L[start][stop] = a[start] + L[start + 1][stop - 1] + a[stop]
            else:
                L[start][stop] = LPSubsequenceLongest(
                    L[start][stop - 1], L[start + 1][stop])

    return L[0][sl - 1]


def LPSubsequenceLongest(string1, string2):
    if len(string1) >= len(string2):
        return string1
    else:
        return string2


def LPSubsequenceLength(str):
    """
    Returns the length of the longest palindromic subsequence within 
    the input string.

    This can be the result of dropping characters to achieve the longest 
    palindrome (e.g. `abdgda` will yield a palindrome of `adgda` because 
    dropping the `b` allows for the longest palindrome, resulting in a 
    returned value of 5.)
    """
    return len(LPSubsequence(str))


print LPSubsequence('dd')
print LPSubsequence('dald')
print LPSubsequence('')
print LPSubsequence(None)
print LPSubsequence('ajsrdvv')
print LPSubsequence('ajsrdvp')

print LPSubsequenceLength('level')
