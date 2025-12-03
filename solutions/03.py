import sys


class Battery:

    def __init__(self, index: int, number: int):
        self.index = index
        self.number = number

    def __lt__(self, other):
        assert isinstance(other, Battery)
        return (self.number, -self.index) < (other.number, -other.index)


def max_joltage(bank: list[Battery]):
    a = max(bank[:-1])
    b = max(bank[a.index + 1 :])
    return 10 * a.number + b.number


total_joltage = 0
for line in sys.stdin.read().splitlines():
    bank = [Battery(i, int(number)) for i, number in enumerate(line)]
    total_joltage += max_joltage(bank)


print(total_joltage)
