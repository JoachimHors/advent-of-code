with open("input.txt", "r") as file:
    lines = file.readlines()


sum = 0

for line in lines:
    line = line.split(':')[-1]
    my_list, winning_list = line.split('|')
    my_list = my_list.split()
    winning_list = winning_list.split()
    matches = 0
    for number in my_list:
        if number in winning_list:
            matches += 1
    if matches > 0:
        sum += 2**(matches-1)

print(sum)
