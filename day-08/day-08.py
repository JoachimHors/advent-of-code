import re
import math

with open("input.txt", "r") as file:
    instructions_line, *nodes = file.read().split("\n\n")

nodes = nodes[0].splitlines()
node_lookup = {}
for node in nodes:
    node_id, node_data = node.split(" = ")
    node_data = re.findall(r"[^\s\(\),]{3}", node_data)
    node_lookup[node_id] = (node_data[0], node_data[1])

current_nodes = [node for node in node_lookup if node[2] == "A"]
cycle_length = []

for current_node in current_nodes:
    instruction_index = 0
    while current_node[2] != "Z":
        instruction = instructions_line[instruction_index % len(
            instructions_line)]
        instruction_index += 1
        if instruction == "L":
            current_node = node_lookup[current_node][0]
        else:
            current_node = node_lookup[current_node][1]
    cycle_length.append(instruction_index)
print(math.lcm(*cycle_length))
