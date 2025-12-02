class Interval:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        assert self.a < self.b

    def __repr__(self):
        return f"{self.a}-{self.b}"

    @classmethod
    def from_input(cls, data: str):
        a, b = data.split("-")
        return Interval(int(a), int(b))

    def contains(self, number: int):
        return self.a <= number <= self.b


intervals = [Interval.from_input(interval) for interval in input().split(",")]


def invalid(number: int):
    string = str(number)
    if len(string) == 1:
        return False
    if string == string[0] * len(string):
        return True

    # All numbers in the input are at most 10 digits
    if len(string) == 10:
        return string == string[:5] * 2 or string == string[:2] * 5
    if len(string) == 9:
        return string == string[:3] * 3
    if len(string) == 8:
        return string == string[:4] * 2 or string == string[:2] * 4
    if len(string) == 6:
        return string == string[:3] * 2 or string == string[:2] * 3
    if len(string) == 4:
        return string == string[:2] * 2
    return False


total = 0
for interval in intervals:
    for number in range(interval.a, interval.b + 1):
        if invalid(number):
            total += number


print(total)
