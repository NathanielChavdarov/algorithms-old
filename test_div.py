import div

def test_div():
    for a, b in [
        (1243, 10),
        (1212637863, 1207),
        (11, 10),
        (101, 10),
        (4, 2),
        (100, 10),
        (2, 8),
        (0, 10),
        (100, 100),
    ]:
        q, m = div.div(a, b)
        assert q == int(a/b), f"unable to calculate {a}/{b}"
        assert m == a%b, f"unable to calculate {a}%{b}"


def test_div_by_zero():
    try:
        div.div(1, 0)
        assert False
    except ValueError:
        pass
