safe = 0

#with open('sample', 'r') as f:
with open('input', 'r') as f:
    reports = [list(map(int, line.strip().split())) for line in f]

for report in reports:
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    if is_increasing or is_decreasing:
        safe += 1

print(safe)