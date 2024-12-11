file_path = "input_1.txt"  # Replace with the path to your file
# file_path = "example.txt"
lefts = []
rights = []
with open(file_path, "r") as file:
    for line in file:
        # Strip any leading/trailing whitespace (including newline characters)
        line = line.strip()
        # Split the line by the 3-space gap
        left, right = line.split("   ")
        lefts.append(int(left))
        rights.append(int(right))

print(lefts)
print(rights)
left_sorted = sorted(lefts)
right_sorted = sorted(rights)

distances = []
for left, right in zip(left_sorted, right_sorted):
    # print(f"Left: {left}, Right: {right}")
    distance = abs(left - right)
    # print(f"Distance: {distance}")
    distances.append(distance)

print(f"Part 1: {sum(distances)}")

part_2_sum = 0
for left in lefts:
    right_num = rights.count(left)
    part_2_sum += right_num * left

print(f"Part 2: {part_2_sum}")