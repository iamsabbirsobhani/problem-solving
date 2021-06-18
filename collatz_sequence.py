# Python 3.8
import time
tCount, cD, m, a = 0, 0, 0, 0
start = time.time()
for n in range(1000000, 0, -1):
    m, c = n, 0
    for i in range(10000):
        if n % 2 == 0:
            n = n/2
        elif n % 2 != 0:
            n = n * 3 + 1
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

end = time.time()

print("Starting number \"{}\" ".format(cD)+"produces the longest chain.")
print("Sequence contains: {} ".format(tCount)+"terms.")
print("Time elapsed: ", (end - start))
