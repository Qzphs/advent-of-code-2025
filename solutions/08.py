import itertools
import math
import sys


class JunctionBox:

    def __init__(self, x: int, y: int, z: int):
        self.parent: JunctionBox | None = None
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_input(cls, data: str):
        return JunctionBox(*map(int, data.split(",")))

    def __repr__(self):
        return f"{self.x},{self.y},{self.z}"

    def ancestor(self):
        if self.parent is None:
            return self
        return self.parent.ancestor()

    def distance(self, other: "JunctionBox"):
        return math.dist(
            (self.x, self.y, self.z),
            (other.x, other.y, other.z),
        )


class Pair:

    def __init__(self, a: JunctionBox, b: JunctionBox):
        self.a = a
        self.b = b
        self.distance = a.distance(b)

    def __repr__(self):
        return f"{repr(self.a)} / {repr(self.b)} (d={self.distance})"

    def connect(self):
        if self.a.ancestor() == self.b.ancestor():
            return
        self.a.ancestor().parent = self.b.ancestor()


class Decoration:

    def __init__(self, junction_boxes: list[JunctionBox]):
        self.junction_boxes = junction_boxes
        self.pairs = sorted(
            (Pair(a, b) for a, b in itertools.combinations(self.junction_boxes, 2)),
            key=lambda pair: pair.distance,
        )

    @classmethod
    def from_input(self, data: list[str]):
        return Decoration([JunctionBox.from_input(line) for line in data])

    def circuit_sizes(self):
        circuits: dict[JunctionBox, int] = {}
        for junction_box in self.junction_boxes:
            ancestor = junction_box.ancestor()
            if ancestor not in circuits:
                circuits[ancestor] = 0
            circuits[ancestor] += 1
        return sorted(circuits.values(), reverse=True)

    def connect_n_shortest(self, n: int):
        for pair in self.pairs[:n]:
            pair.connect()


decoration = Decoration.from_input(sys.stdin.read().splitlines())
decoration.connect_n_shortest(1000)
print(math.prod(decoration.circuit_sizes()[:3]))
