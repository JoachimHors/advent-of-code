with open("input.txt", "r") as file:
    lines = file.readlines()


def check_lines(lines, current_line, scratch_dict):
    if current_line in scratch_dict.keys():
        scratch_dict[current_line] += 1
    else:
        scratch_dict[current_line] = 1

    line = lines[current_line].split(':')[-1]
    my_list, winning_list = line.split('|')
    my_list = my_list.split()
    winning_list = winning_list.split()
    matches = 0

    for number in my_list:
        if number in winning_list:
            matches += 1

    for i in range(1, matches + 1):
        if current_line + i in scratch_dict.keys():
            scratch_dict[current_line + i] += scratch_dict[current_line]
        else:
            scratch_dict[current_line + i] = scratch_dict[current_line]

    return sum(list(scratch_dict.values())) if current_line >= len(lines) - 1 else check_lines(lines, current_line + 1,
                                                                                               scratch_dict)


print(check_lines(lines, 0, {}))