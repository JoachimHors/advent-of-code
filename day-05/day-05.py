# Complete redesign of the approach to the problem using ranges

with open("input.txt", "r") as file:
    input_line, *mapping_blocks = file.read().split("\n\n")

seed_inputs = list(map(int, input_line.split(":")[1].split()))

seed_ranges = []

for i in range(0, len(seed_inputs), 2):
    seed_start, range_length = seed_inputs[i], seed_inputs[i + 1]
    seed_ranges.append((seed_start, seed_start + range_length))

for mapping_block in mapping_blocks:
    category_mappings = []
    for line in mapping_block.splitlines()[1:]:
        category_mappings.append(list(map(int, line.split())))
    transformed_ranges = []
    while len(seed_ranges) > 0:
        range_start, range_end = seed_ranges.pop()
        for dest_start, src_start, src_length in category_mappings:
            overlap_start = max(range_start, src_start)
            overlap_end = min(range_end, src_start + src_length)
            if overlap_start < overlap_end:
                transformed_ranges.append(
                    (overlap_start - src_start + dest_start, overlap_end - src_start + dest_start))
                if overlap_start > range_start:
                    seed_ranges.append((range_start, overlap_start))
                if range_end > overlap_end:
                    seed_ranges.append((overlap_end, range_end))
                break
        else:
            transformed_ranges.append((range_start, range_end))
    seed_ranges = transformed_ranges

print(min(seed_ranges)[0])
