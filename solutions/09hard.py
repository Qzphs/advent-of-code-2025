# forgive me for single letter hell

# Throughout the solution:
# t = true (same as input)
# c = compressed (same as grid indices)


import itertools
import sys


class Tile:

    def __init__(self, tx: int, ty: int):
        self.tx = tx
        self.ty = ty

    @classmethod
    def from_input(cls, data: str):
        return Tile(*map(int, data.split(",")))

    def area(self, other: "Tile"):
        return (abs(self.tx - other.tx) + 1) * (abs(self.ty - other.ty) + 1)


class CoordinateConverter:

    def __init__(self, coordinates: list[int]):
        self.coordinates = sorted(set(coordinates))

    def c(self, number: int):
        return self.coordinates.index(number) * 2

    def t(self, number: int):
        return self.coordinates[number // 2]


class Grid:

    def __init__(self, tiles: list[Tile]):
        self.tiles = tiles
        self.xc = CoordinateConverter([tile.tx for tile in tiles])
        self.yc = CoordinateConverter([tile.ty for tile in tiles])
        self.cwidth = len(self.xc.coordinates) * 2
        self.cheight = len(self.yc.coordinates) * 2
        self.cpoints = [[False] * self.cheight for _ in range(self.cwidth)]

    def _add_tline(self, a: Tile, b: Tile):
        """Add line of cpoints between two tiles to grid."""
        if a.tx == b.tx:
            cx = self.xc.c(a.tx)
            min_cy = self.yc.c(min(a.ty, b.ty))
            max_cy = self.yc.c(max(a.ty, b.ty))
            for cy in range(min_cy, max_cy + 1):
                self.cpoints[cx][cy] = True
        else:
            assert a.ty == b.ty
            cy = self.yc.c(a.ty)
            min_cx = self.xc.c(min(a.tx, b.tx))
            max_cx = self.xc.c(max(a.tx, b.tx))
            for cx in range(min_cx, max_cx + 1):
                self.cpoints[cx][cy] = True

    def add_all_tlines(self):
        """Step 1. Add all lines consecutive pairs of tiles."""
        for a, b in itertools.pairwise(self.tiles):
            self._add_tline(a, b)
        self._add_tline(self.tiles[0], self.tiles[-1])

    def fill_area(self):
        """Step 2. Use BFS to find area with red/green tiles."""
        # Start by guessing the middle point and hoping it's inside :zany_face:
        bfs_queue = {(self.cwidth // 2, self.cheight // 2)}

        while bfs_queue:
            cx, cy = bfs_queue.pop()
            self.cpoints[cx][cy] = True
            if not self.cpoints[cx - 1][cy]:
                bfs_queue.add((cx - 1, cy))
            if not self.cpoints[cx + 1][cy]:
                bfs_queue.add((cx + 1, cy))
            if not self.cpoints[cx][cy - 1]:
                bfs_queue.add((cx, cy - 1))
            if not self.cpoints[cx][cy + 1]:
                bfs_queue.add((cx, cy + 1))

    def _valid_rectangle(self, a: Tile, b: Tile):
        # Probably safe to ignore 1xn or nx1 rectangles
        if a.tx == b.tx:
            return False
        if a.ty == b.ty:
            return False

        min_cx = self.xc.c(min(a.tx, b.tx))
        max_cx = self.xc.c(max(a.tx, b.tx))
        min_cy = self.yc.c(min(a.ty, b.ty))
        max_cy = self.yc.c(max(a.ty, b.ty))

        for cx in range(min_cx, max_cx + 1):
            if not self.cpoints[cx][min_cy]:
                return False
            if not self.cpoints[cx][max_cy]:
                return False
        for cy in range(min_cy, max_cy + 1):
            if not self.cpoints[min_cx][cy]:
                return False
            if not self.cpoints[max_cx][cy]:
                return False

        return True

    def tile_areas(self):
        """Step 3. Look for tile areas again."""
        return (
            a.area(b)
            for a, b in itertools.combinations(self.tiles, 2)
            if self._valid_rectangle(a, b)
        )


tiles = [Tile.from_input(line) for line in sys.stdin.read().splitlines()]
grid = Grid(tiles)

grid.add_all_tlines()
grid.fill_area()

print(max(grid.tile_areas()))
