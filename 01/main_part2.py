from collections import defaultdict

with open("input.txt", "r") as f:
    first_column = []
    second_column = []

    for line in f:
        columns = line.strip().split()
        first_column.append(int(columns[0]))
        second_column.append(int(columns[1]))

number_count_dict = defaultdict(int)

for num in second_column:
    number_count_dict[num] += 1

similarity_score = 0

for num in first_column:
    similarity_score += num * number_count_dict[num]

print("Answer =", similarity_score)