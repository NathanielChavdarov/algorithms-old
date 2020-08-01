import math


def primetester(a: int) -> bool:
    if a < 2:
        return False
    end = int(math.sqrt(a))
    for i in range(2, end+1):
        if a % i == 0:
            return False
    return True


def primetester2(a: int) -> bool:
    if a <= 3:
        return a > 1
    if a % 2 == 0 or a % 3 == 0:
        return False

    i = 5

    while i * i <= a:
        if a % i == 0 or a % (i+2) == 0:
            return False
        i += 6
    return True


def generate_primetester2function(n):
    def wibble():
        return primetester2(n)
    return wibble


if __name__ == "__main__":
    import timeit
    x = generate_primetester2function(904265051)
    n = 1
    while True:
        t = timeit.timeit(x, number=n)
        if t < 0.5:
            n <<= 1
        else:
            break
    print(f"Time = {t}, Iterations = {n}, time per iteration = {t/n}")
    # import time
    # t = time.perf_counter()
    # fib1(30)
    # t2 = time.perf_counter()
    # print(t2 - t)
