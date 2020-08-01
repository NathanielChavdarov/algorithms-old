def fib0(n: int) -> int:
    if n == 0:
        return 0
    # Setting numbers to the variables
    y = 1
    z = 1
    x = y + z

    for i in range(n-2):
        # Updating the y variable
        y = x

        # Creating the next term
        x = y + z
        # Updating the Z variable
        z = y

    return z


def fib1(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib1(n-1) + fib1(n-2)


def fib2(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    sequence = [0, 1]
    while len(sequence) <= n:
        sequence.append(sequence[-1]+sequence[-2])
    return sequence[-1]


def generate_fib1function(n):
    def wibble():
        return fib1(n)
    return wibble


def generate_fib0function(n):
    def wibble():
        return fib0(n)
    return wibble


def generate_fib2function(n):
    def wibble():
        return fib2(n)
    return wibble


if __name__ == "__main__":
    import timeit
    x = generate_fib2function(30)
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
