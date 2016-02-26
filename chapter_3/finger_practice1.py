x = int(raw_input('Enter an integer: '))
root = 0
pwr = 1

while x != root ** pwr:
    pwr = pwr + 1
    if pwr > 5:
        root = root + 1
        pwr = 0


if x == root ** pwr:
    print 'This is answer : root = ', root, ' pwr = ', pwr

else:
    print 'Not have integer', x
