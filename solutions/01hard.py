import sys


class Dial:

    def __init__(self):
        self.number = 50
        self.count = 0

    def turn_left(self, clicks: int):
        self.count += clicks // 100
        new_number = self.number - (clicks % 100)
        if new_number <= 0 < self.number:
            self.count += 1
        self.number = new_number % 100

    def turn_right(self, clicks: int):
        self.count += clicks // 100
        new_number = self.number + (clicks % 100)
        if self.number < 100 <= new_number:
            self.count += 1
        self.number = new_number % 100


dial = Dial()

for line in sys.stdin.read().splitlines():
    direction = line[0]
    distance = int(line[1:])
    if direction == "L":
        dial.turn_left(distance)
    else:
        dial.turn_right(distance)

print(dial.count)
