import sys


class Manifold:

    def __init__(self):
        self.beams: dict[int, int] = {}

    def split(self, layer: list[str]):
        beams = {i: 0 for i in range(len(layer))}
        for i, point in enumerate(layer):
            if point == "S":
                beams[i] += 1
            elif point == "^" and i in self.beams:
                beams[i - 1] += self.beams[i]
                beams[i + 1] += self.beams[i]
            elif point == "." and i in self.beams:
                beams[i] += self.beams[i]
        self.beams = beams


manifold = Manifold()
for layer in sys.stdin.read().splitlines():
    manifold.split(layer)

print(sum(manifold.beams.values()))
