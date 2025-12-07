import sys


class Manifold:

    def __init__(self):
        self.beams: set[int] = set()
        self.splits: int = 0

    def split(self, layer: list[str]):
        beams: set[int] = set()
        for i, point in enumerate(layer):
            if point == "S":
                beams.add(i)
            elif point == "^" and i in self.beams:
                beams.add(i - 1)
                beams.add(i + 1)
                self.splits += 1
            elif point == "." and i in self.beams:
                beams.add(i)
        self.beams = beams


manifold = Manifold()
for layer in sys.stdin.read().splitlines():
    manifold.split(layer)

print(manifold.splits)
