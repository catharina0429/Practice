from collections.abc import Iterable

def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    # your code here
    res = []
    for i in donuts:
        if i == 0:
            res.append(i)
        res.append(i)
    return res


print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]
print("The mission is done! Click 'Check Solution' to earn rewards!")