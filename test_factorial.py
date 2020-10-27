import math
import factorial as f

tests = [
    0,
    1,
    2,
    5,
    10,
    25,
    50,
    ]


def test_factorial():
    for i in tests:
        assert f.factorial(i) == int(math.factorial(i))
