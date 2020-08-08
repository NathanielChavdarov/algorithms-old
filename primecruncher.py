import primegen as p


def primecruncher():
    fileHandler = open("primes.txt", "w")
    fileHandler.write("2\n3\n")
    for j in range(5, 1000000+1):
        if p.primetester2(j):
            fileHandler.write(str(j) + "\n")
    fileHandler.close()


if __name__ == "__main__":
    import timeit
    n = 1
    while True:
        t = timeit.timeit(primecruncher, number=n)
        if t < 0.5:
            n <<= 1
        else:
            break
    print(f"Time = {t}, Iterations = {n}, time per iteration = {t/n}")
