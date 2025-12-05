import sys


class Interval:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b  # b is inclusive

    @classmethod
    def from_input(cls, data: str):
        a, b = data.split("-")
        return Interval(int(a), int(b))

    def __repr__(self):
        return f"({self.a} - {self.b})"

    def overlaps(self, other: "Interval"):
        return (self.a <= other.a <= self.b + 1) or (self.a - 1 <= other.b <= self.b)

    def merge(self, other: "Interval"):
        """
        Update this interval to also include the other one.

        (The other one will be discarded.)
        """
        self.a = min(self.a, other.a)
        self.b = max(self.b, other.b)


class Inventory:

    def __init__(self):
        self.intervals: list[Interval] = []

    def add(self, interval: Interval):
        unmerged_intervals: list[Interval] = []
        for existing_interval in self.intervals:
            if existing_interval.overlaps(interval):
                interval.merge(existing_interval)
            else:
                unmerged_intervals.append(existing_interval)
        self.intervals.clear()
        self.intervals.extend(unmerged_intervals)
        self.intervals.append(interval)

    def __repr__(self):
        return repr(self.intervals)

    def contains(self, ingredient: int):
        """
        Check whether ingredient is in any interval.

        The ingredient being present means it is fresh.
        """
        return any(interval.a <= ingredient <= interval.b for interval in self.intervals)


intervals, queries = sys.stdin.read().split("\n\n")
inventory = Inventory()


for line in intervals.splitlines():
    interval = Interval.from_input(line)
    inventory.add(interval)

n_fresh = 0
for line in queries.splitlines():
    ingredient = int(line)
    if inventory.contains(ingredient):
        n_fresh += 1

print(n_fresh)
