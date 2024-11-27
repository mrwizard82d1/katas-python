def karate_chop(item, seq):
    start = 0
    end = len(seq) - 1
    candidate = (start + end) // 2
    while start <= candidate <= end:
        if seq[candidate] == item:
            return candidate

        if item < seq[start] or seq[end] < item:
            return -1

        elif seq[start] <= item < seq[candidate]:
            end = candidate - 1
            candidate = (start + end) // 2
        elif seq[candidate] < item <= seq[end]:
            start = candidate + 1
            candidate = (start + end) // 2
        else:
            raise Exception('Oops')

    return -1


def test_simple_1():
    assert(karate_chop(1, [0, 1, 2]) == 1)


def test_simple_0():
    assert(karate_chop(0, [0, 1, 2]) == 0)


def test_simple_2():
    assert(karate_chop(2, [0, 1, 2]) == 2)


def test_greater_than_largest():
    assert(karate_chop(3, [0, 1, 2]) == -1)


def test_less_than_smallest():
    assert(karate_chop(-1, [0, 1, 2]) == -1)


def test_missing():
    assert(karate_chop(1, [0, 2, 3]) == -1)
