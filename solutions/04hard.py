import sys


class Grid:

    def __init__(self, rows: list[list[str]]):
        self.rows = rows

    @classmethod
    def from_input(cls, data: list[str]):
        return Grid([list(row) for row in data])

    def has_roll(self, u: int, v: int):
        if not 0 <= u < len(self.rows):
            return False
        if not 0 <= v < len(self.rows[0]):
            return False
        return self.rows[u][v] == "@"

    def has_accessible_roll(self, u: int, v: int):
        if not self.has_roll(u, v):
            return False
        neighbours = [
            self.has_roll(u - 1, v - 1),
            self.has_roll(u - 1, v),
            self.has_roll(u - 1, v + 1),
            self.has_roll(u, v + 1),
            self.has_roll(u + 1, v + 1),
            self.has_roll(u + 1, v),
            self.has_roll(u + 1, v - 1),
            self.has_roll(u, v - 1),
        ]
        return sum(neighbours) < 4

    @property
    def removed(self):
        return "".join("".join(row) for row in self.rows).count("x")


grid = Grid.from_input(sys.stdin.read().splitlines())


roll_removed = True
while roll_removed:
    roll_removed = False
    for u in range(len(grid.rows)):
        for v in range(len(grid.rows[0])):
            if not grid.has_accessible_roll(u, v):
                continue
            grid.rows[u][v] = "x"
            roll_removed = True


print(grid.removed)
