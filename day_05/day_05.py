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