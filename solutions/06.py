import sys


lines = sys.stdin.read().splitlines()
rows = [list(map(int, line.split())) for line in lines[:-1]]
operations = lines[-1].split()

n_problems = len(operations)
grand_total = 0
for i in range(n_problems):
    if operations[i] == "+":
        result = 0
        for row in rows:
            result += row[i]
    else:
        result = 1
        for row in rows:
            result *= row[i]
    grand_total += result

print(grand_total)
