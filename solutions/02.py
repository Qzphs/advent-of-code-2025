class Interval:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        assert self.a < self.b

    @classmethod
    def from_input(cls, data: str):
        a, b = data.split("-")
        return Interval(int(a), int(b))

    def contains(self, number: int):
        return self.a <= number <= self.b


intervals = [Interval.from_input(interval) for interval in input().split(",")]
max_number = max(max(interval.a, interval.b) for interval in intervals)


i = 0
number = int(str(i) + str(i))
total = 0
while number < max_number:
    if any(interval.contains(number) for interval in intervals):
        total += number
    i += 1
    number = int(str(i) + str(i))


print(total)
