# Python 3.8

tCount = 0
cD = 0
m = 0
a = 0
for n in range(100, 0, -1):
    m = n
    c = 0
    print("For {}".format(n)+" Collatz sequences: ")
    for i in range(10000):
        if n % 2 == 0:
            n = n/2
        elif n % 2 is not 0:
            n = n * 3 + 1
        print("    {}".format(n))
        if n >= 1:
            c = c + 1
        if n == 1:
            break
    c = c + 1
    if tCount < c and cD >= a:
        tCount = c
        cD = m
        a = cD
        n = m
    print("Total Collatz terms: {}".format(c))
    print("\n")


print("Starting number \"{}\" ".format(cD)+"produces the longest chain.")
print("Sequence contains: {} ".format(tCount)+"terms.")
