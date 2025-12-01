import sys


dial = 50
count = 0


for line in sys.stdin.read().splitlines():

    direction = line[0]
    distance = int(line[1:])
    if direction == "L":
        distance = -distance

    dial = (dial + distance) % 100
    if dial == 0:
        count += 1

print(count)
