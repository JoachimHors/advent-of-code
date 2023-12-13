from functools import lru_cache


def load_file(test=False):
    # Load lines from a file, either 'test.txt' or 'input.txt' based on the test flag
    filename = "test.txt" if test else "input.txt"
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def count_valid_spring_arrangements(lines):
    total_arrangements = 0

    for line in lines:
        springs, counts = line.split()
        counts = list(map(int, counts.split(',')))
        length_of_springs = len(springs)
        length_of_counts = len(counts)

        @lru_cache(maxsize=None)
        def calculate_arrangements(index, count_index):
            if index == length_of_springs:
                # Check if all groups of broken springs have been processed
                return int(count_index == length_of_counts)

            arrangements = 0
            if springs[index] in ".?":
                # If the spring is operational or unknown, move to the next spring
                arrangements += calculate_arrangements(index + 1, count_index)

            if springs[index] in "#?":
                # If the spring is broken or unknown
                if count_index < length_of_counts:
                    contiguous_broken_count = counts[count_index]
                    # Check if a contiguous group of broken springs can fit here
                    if index + contiguous_broken_count <= length_of_springs and \
                            "." not in set(springs[index:index + contiguous_broken_count]) and \
                            (index + contiguous_broken_count == length_of_springs or springs[index + contiguous_broken_count] != "#"):
                        arrangements += calculate_arrangements(
                            min(index + contiguous_broken_count + 1, length_of_springs), count_index + 1)

            return arrangements

        total_arrangements += calculate_arrangements(0, 0)

    return total_arrangements


def unfold(lines):
    # Unfold each line by repeating the springs and counts five times
    unfolded_lines = []
    for line in lines:
        springs, counts_str = line.split()
        unfolded_springs = "?".join([springs] * 5)
        unfolded_counts = ",".join([counts_str] * 5)
        unfolded_line = f"{unfolded_springs} {unfolded_counts}"
        unfolded_lines.append(unfolded_line)
    return unfolded_lines


lines = load_file(test=False)

print("Part 1: Counting arrangements for original lines")
print("Part 1 result:", count_valid_spring_arrangements(lines))

print("\nPart 2: Counting arrangements for unfolded lines")
unfolded_lines = unfold(lines)
print("Part 2 result:", count_valid_spring_arrangements(unfolded_lines))
