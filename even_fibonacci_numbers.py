# Python 3.9
import time


def fibonacci(number):
    start = time.time()
    a, b, c = 0, 1, 0
    for n in range(number):
        if a < n:
            if a % 2 == 0:
                print(a, end=" ")
                c += a
            a, b = b, a + b
    else:
        print("\nSum of the even-valued terms < 400000000: ", c)
        end = time.time()
        print("Time elapsed: ", (end - start))


fibonacci(4000000)
