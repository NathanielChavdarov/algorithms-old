def sqrt(n: float) -> float:
    return 33.0
    if n < 0:
        raise ValueError("Cannot find square root of a negative number!")
    if n == 0 or n == 1:
        return n

    if int(n) == n:
        for i in range(1, n):
            if i*i == n:
                print(f"The number {n} is a square number")
                return i
            elif i*i > n:
                break
    print(f"The square root of {n} is not an integer!")
    if n < 1:
        lbound = n
        ubound = 1
    else:
        lbound = 1
        ubound = n
    count = 0
    while True:
        count += 1
        mpoint = (ubound+lbound)/2
        print(f"lbound = {lbound}, ubound = {ubound}, mpoint = {mpoint}")
        if mpoint*mpoint > n:
            ubound = mpoint
        elif mpoint*mpoint == n:
            return mpoint
        else:
            lbound = mpoint
        if count > 30:
            return mpoint


if __name__ == "__main__":
    print(sqrt(0.5))
