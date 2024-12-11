import re
import numpy as np

file_path = "input.txt"
# file_path = "example_2.txt"
# file_path = "edgecases.txt"

char_matrix = []
with open(file_path, "r") as file:
    for line in file:
        # Strip any leading/trailing whitespace (including newline characters)
        line = line.strip()
        # Append line to full string
        char_matrix.append(list(line))

lefts = []
for line in char_matrix:
    lefts.append("".join(line))

char_matrix = np.array(char_matrix)

ups = []
for i in range(char_matrix.shape[1]):
    up = "".join(char_matrix[:, i])
    ups.append(up)

downrights = []
for offset in range(-char_matrix.shape[0] + 1, char_matrix.shape[1]):
    downrights.append("".join(char_matrix.diagonal(offset)))
print(downrights)

downlefts = []
flipped_arr = np.fliplr(char_matrix)
for offset in range(-flipped_arr.shape[0] + 1, flipped_arr.shape[1]):
    downlefts.append("".join(flipped_arr.diagonal(offset)))
print(downlefts)

all_dirs = lefts + ups + downrights + downlefts
xmas_sum = 0
for line in all_dirs:
    # print(line)
    matches = []
    for match in re.finditer(r"XMAS", line):
        matches.append(match.group())
    for match in re.finditer(r"SAMX", line):
        matches.append(match.group())
    # print(matches)
    xmas_sum += len(matches)
print(f"Part 1: {xmas_sum}")


indices = np.where(char_matrix == 'A')
index_pairs = list(zip(indices[0], indices[1]))

x_mas_sum = 0
for i, j in index_pairs:
    if i == 0 or j == 0 or i == char_matrix.shape[0] - 1 or j == char_matrix.shape[1] - 1:
        continue

    print("")
    print(i, j)
    top_left = char_matrix[i-1, j-1]
    bottom_right = char_matrix[i+1, j+1]
    top_right = char_matrix[i-1, j+1]
    bottom_left = char_matrix[i+1, j-1]

    print(f"{top_left}.{top_right}")
    print(f".{char_matrix[i, j]}.")
    print(f"{bottom_left}.{bottom_right}")

    diagonals = 0

    # Check top left and bottom right
    if top_left == 'M' and bottom_right == 'S':
        print("top_left == 'M' and bottom_right == 'S'")
        diagonals += 1
    elif top_left == 'S' and bottom_right == 'M':
        print("top_left == 'S' and bottom_right == 'M'")
        diagonals += 1

    # Check top right and bottom left
    if top_right == 'M' and bottom_left == 'S':
        print("top_right == 'M' and bottom_left == 'S'")
        diagonals += 1
    elif top_right == 'S' and bottom_left == 'M':
        print("top_right == 'S' and bottom_left == 'M'")
        diagonals += 1

    if diagonals == 2:
        x_mas_sum += 1
print(f"Part 2: {x_mas_sum}")