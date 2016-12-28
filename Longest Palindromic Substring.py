
def LPSubstring(a):
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
    return a[palPosStart:(palPosStart + maxPalLength)]


print LPSubstring('davad')
print LPSubstring('davsad')
print LPSubstring(None)
print LPSubstring('')
print LPSubstring('davaD')
