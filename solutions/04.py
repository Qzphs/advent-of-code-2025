import sys


class Grid:

    def __init__(self, rows: list[str]):
        self.rows = rows

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


grid = Grid(sys.stdin.read().splitlines())


accessible_rolls = 0
for u in range(len(grid.rows)):
    for v in range(len(grid.rows[0])):
        if not grid.has_accessible_roll(u, v):
            continue
        accessible_rolls += 1


print(accessible_rolls)
