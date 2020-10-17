import sort as s


def test_emptylist():
    result = s.sort([])
    assert result == []


def listlen1(x):
    result = s.sort([x])
    assert result == [x]


def test_listlen1():
    listlen1(2)


def test_anylenlist():
    testlist = [1, 2, 4, 0, 1.099, -12, -2, -4.56, 2, -3]
    sortlist = [-12, -4.56, -3, -2, 0, 1, 1.099, 2, 2, 4]

    result = s.sort(testlist)

    assert result == sortlist
