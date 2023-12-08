import re

with open("input.txt", "r") as file:
    instructions_line, *nodes = file.read().split("\n\n")

nodes = nodes[0].splitlines()

node_lookup = {}
for node in nodes:
    node_id, node_data = node.split(" = ")
    node_data = re.findall(r"[A-Z]{3}", node_data)
    node_lookup[node_id] = (node_data[0], node_data[1])

current_node = "AAA"
instruction_index = 0

while current_node != "ZZZ":
    instruction = instructions_line[instruction_index % len(instructions_line)]
    instruction_index += 1

    if instruction == "L":
        current_node = node_lookup[current_node][0]
    else:
        current_node = node_lookup[current_node][1]

print(instruction_index)
