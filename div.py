from typing import Tuple


def div(a: int, b: int) -> Tuple[int, int]:
    if b == 0:
        raise ValueError("Cannot divide by 0!")
    quotient = 0
    save = b
    while a >= save:
        count = 0
        while a >= b:
            b <<= 1
            count += 1
        b >>= 1
        count -= 1
        a -= b
        quotient += 1 << count
        b = save
    return quotient, a
