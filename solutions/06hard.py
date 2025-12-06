import math
import sys


lines = sys.stdin.read().splitlines()
n_columns = len(lines[0])

numbers = [""] * n_columns
operators = [""] * n_columns


for line in lines[:-1]:
    for i, symbol in enumerate(line):
        numbers[i] += symbol
for i, symbol in enumerate(lines[-1]):
    operators[i] = symbol


grand_total = 0
problem: list[int] = []
operator = " "
for i in range(n_columns):
    if operators[i] != " ":
        operator = operators[i]
    if not numbers[i].isspace():
        problem.append(int(numbers[i].strip()))
        continue

    # Otherwise blank column found, which means all previous numbers
    # are part of the same problem
    if operator == "+":
        grand_total += sum(problem)
        problem.clear()
    else:
        grand_total += math.prod(problem)
        problem.clear()

# Do this again for the last problem
if operator == "+":
    grand_total += sum(problem)
    problem.clear()
else:
    grand_total += math.prod(problem)
    problem.clear()

print(grand_total)
