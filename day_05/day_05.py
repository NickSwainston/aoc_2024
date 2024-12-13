import re
import numpy as np

file_path = "input.txt"
# file_path = "example.txt"
# file_path = "edgecases.txt"

lines = []
with open(file_path, "r") as file:
    print(str(file))
    for line in file:
        lines.append(line.strip())

blank_line_index = lines.index('') if '' in lines else len(lines)
page_order_rules = [line.split("|") for line in lines[:blank_line_index]]
updates = [line.split(",") for line in lines[blank_line_index + 1:]]

print(page_order_rules)
print(updates)

def is_valid_update(update, rules):
    for before_rule, after_rule in rules:
        if before_rule in update and after_rule in update:
            # print(f"Before: {before_rule} After: {after_rule}")
            before_indexes = [index for index, value in enumerate(update) if value == before_rule]
            after_indexes = [index for index, value in enumerate(update) if value == after_rule]
            for before_index in before_indexes:
                for after_index in after_indexes:
                    if before_index > after_index:
                        print("Invalid")
                        print(f"Before: {before_rule} After: {after_rule}")
                        return False, before_index, after_index
    return True, None, None

invalid_sum = 0
fixed_sum = 0
for update in updates:
    valid, before_index, after_index = is_valid_update(update, page_order_rules)
    if valid:
        print("Valid")
        middle_index = len(update) // 2
        invalid_sum += int(update[middle_index])
    else:
        print("Invalid")
        while not valid:
            before_value = int(update[before_index])
            after_value = int(update[after_index])
            update[before_index] = str(after_value)
            update[after_index] = str(before_value)
            valid, before_index, after_index = is_valid_update(update, page_order_rules)
        middle_index = len(update) // 2
        print(update[middle_index])
        fixed_sum += int(update[middle_index])

print(f"Part 1: {invalid_sum}")
print(f"Part 2: {fixed_sum}")
