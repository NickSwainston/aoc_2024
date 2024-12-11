file_path = "input.txt"
# file_path = "example.txt"
# file_path = "edgecases.txt"

floors = []
with open(file_path, "r") as file:
    for line in file:
        # Strip any leading/trailing whitespace (including newline characters)
        line = line.strip()
        # Split the line by the 3-space gap
        floors.append([int(i) for i in line.split(" ")])


def is_floor_safe(floor):
    decreasing = False
    increasing = False
    safe = True
    for level_i in range(len(floor)-1):
        level = floor[level_i]
        next_level = floor[level_i+1]
        if level == next_level:
            print("No change")
            safe = False
            break
        if abs(level - next_level) > 3:
            print("Too big a change")
            safe = False
            break
        if level > next_level:
            decreasing = True
        if level < next_level:
            increasing = True
        if increasing and decreasing:
            print("Both increasing and decreasing")
            safe = False
            break
    return safe

unsafe_floors = []
print(floors)
safe_sum = 0
a_unsafe_sum = 0
for floor in floors:
    print("")
    print(floor)
    safe = is_floor_safe(floor)

    if safe:
        print("Safe")
        safe_sum += 1
        a_unsafe_sum += 1
    else:
        unsafe_floors.append(floor)
        print("remove level check")
        for level_to_remove in range(len(floor)):
            new_floor = floor.copy()
            del new_floor[level_to_remove]
            print(new_floor)

            safe = is_floor_safe(new_floor)
            if safe:
                print("Now safe")
                a_unsafe_sum += 1
                break



print(f"Part 1: {safe_sum}")
print(f"Part 2: {a_unsafe_sum}")


