def picalc() -> float:
    p = 10000
    counter = 0

    x = 0
    pp = p*p
    while x <= p:
        y = 0
        xx = x*x
        while y <= p:
            yy = y*y
            d = xx + yy
            if d <= pp:
                counter += 1
            y += 1
        x += 1
    pi = counter * 4 / pp
    print(pi)
    return pi


if __name__ == "__main__":
    import timeit
    n = 1
    while True:
        t = timeit.timeit(picalc, number=n)
        if t < 0.5:
            n <<= 1
        else:
            break
    print(f"Time = {t}, Iterations = {n}, time per iteration = {t/n}")
