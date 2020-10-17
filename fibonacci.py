def fib(n: int) -> int:
    if n == 0:
        return 0
    y = 1
    z = 1
    x = 2
    for i in range(n-2):
        y = x
        x = y + z
        z = y

    return z


if __name__ == "__main__":
    def generate_fibfunction(n):
        def wibble():
            return fib(n)
        return wibble

    import timeit
    x = generate_fibfunction(30)
    n = 1
    while True:
        t = timeit.timeit(x, number=n)
        if t < 0.5:
            n <<= 1
        else:
            break
    print(f"Time = {t}, Iterations = {n}, time per iteration = {t/n}")
