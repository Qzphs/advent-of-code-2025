import itertools
import sys


class Tile:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def from_input(cls, data: str):
        return Tile(*map(int, data.split(",")))

    def area(self, other: "Tile"):
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)


tiles = [Tile.from_input(line) for line in sys.stdin.read().splitlines()]


print(max(a.area(b) for a, b in itertools.combinations(tiles, 2)))
