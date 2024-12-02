safe = 0

def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)
    return is_increasing or is_decreasing

#with open('sample', 'r') as f:
with open('input', 'r') as f:
    reports = [list(map(int, line.strip().split())) for line in f]

for report in reports:
    if is_safe(report):
        safe += 1
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                safe += 1
                break



print(safe)