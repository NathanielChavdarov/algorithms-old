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


def test_fibonacci():
    # The slow function
    for i, fib_i in answers:
        assert f.fib(i) == fib_i
