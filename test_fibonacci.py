import fibonacci as f

answers = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (20, 6765),
    (30, 832040),
]


def test_fibonacci0():
    # The slow function
    for i, fib_i in answers:
        assert f.fib0(i) == fib_i


def test_fibonacci1():
    # The slow function
    for i, fib_i in answers:
        assert f.fib1(i) == fib_i


def test_fibonacci2():
    # The quicker function
    answers2 = answers
    answers2.append((40, 102334155))
    for i, fib_i in answers2:
        assert f.fib2(i) == fib_i
