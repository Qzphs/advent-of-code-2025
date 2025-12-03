import sys


class Battery:

    def __init__(self, index: int, number: int):
        self.index = index
        self.number = number

    def __lt__(self, other):
        assert isinstance(other, Battery)
        return (self.number, -self.index) < (other.number, -other.index)


def max_joltage(bank: list[Battery]):
    joltage = 0
    for i in range(11, 0, -1):
        highest = max(bank[:-i])
        bank = bank[highest.index + 1 :]
        for index, battery in enumerate(bank):
            battery.index = index
        joltage *= 10
        joltage += highest.number
    last = max(bank)
    joltage *= 10
    joltage += last.number
    return joltage


total_joltage = 0
for line in sys.stdin.read().splitlines():
    bank = [Battery(i, int(number)) for i, number in enumerate(line)]
    total_joltage += max_joltage(bank)


print(total_joltage)
