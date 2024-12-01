with open("input.txt", "r") as f:
    first_column = []
    second_column = []

    for x in f:
        columns = x.strip().split()
        first_column.append(int(columns[0]))
        second_column.append(int(columns[1]))

first_column.sort()
second_column.sort()

total_sum = 0

for i in range(len(first_column)):
    total_sum += abs(first_column[i] - second_column[i])

print("Answer =", total_sum)