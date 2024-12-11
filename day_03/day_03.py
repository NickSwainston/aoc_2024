import re

file_path = "input.txt"
# file_path = "example.txt"
# file_path = "edgecases.txt"

full_str = ""
with open(file_path, "r") as file:
    for line in file:
        # Strip any leading/trailing whitespace (including newline characters)
        line = line.strip()
        # Append line to full string
        full_str += line

# Regex pattern
pattern = r"mul\(\d+,\d+\)"

# Find all matches
matches = [(match.group(), match.start(), match.end()) for match in re.finditer(r"mul\(\d+,\d+\)", full_str)]

does = [match.start() for match in re.finditer(r"do\(\)", full_str)]
donts = [match.start() for match in re.finditer(r"don\'t\(\)", full_str)]

print("Matches:", matches)
print("does:", does)
print("donts:", donts)

do_donts = [True]
for i in range(1, len(full_str)):
    if i in does:
        do_donts.append(True)
    elif i in donts:
        do_donts.append(False)
    else:
        do_donts.append(do_donts[-1])

mul_sum = 0
for match, start, end in matches:
    num_1, num_2 = map(int, match[4:-1].split(","))
    mul_sum += num_1 * num_2

print(f"Part 1: {mul_sum}")

do_mul_sum = 0
for match, start, end in matches:
    print(do_donts[start])
    if do_donts[start]:
        num_1, num_2 = map(int, match[4:-1].split(","))
        do_mul_sum += num_1 * num_2

print(f"Part 2: {do_mul_sum}")
