def question2(str):
    """
    Return the longest contiguous palindrome within input string
    """
    if str is None or str == '':
        return ''

    str = str.lower()

    maxPalLength = 1
    n = len(str)
    palPosStart = 0

    start = 0
    stop = 0

    for index in xrange(1, n):
        # Even number palindrome validations
        start = index - 1
        stop = index

        while start >= 0 and stop < n and str[start] == str[stop]:
            if stop - start + 1 > maxPalLength:
                palPosStart = start
                maxPalLength = stop - start + 1
            start -= 1
            stop += 1

        # Odd number palindrome validations
        start = index - 1
        stop = index + 1

        while start >= 0 and stop < n and str[start] == str[stop]:
            if stop - start + 1 > maxPalLength:
                palPosStart = start
                maxPalLength = stop - start + 1
            start -= 1
            stop += 1
    return str[palPosStart:(palPosStart + maxPalLength)]


print question2('davad')
print question2('davsad')
print question2(None)
print question2('')
print question2('davaD')
print question2('14097415k')
print question2('14797415k')
print question2('awabdwcb')
print question2('$%@##%')
