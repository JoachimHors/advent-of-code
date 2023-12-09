with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [[int(y) for y in (x.replace("\n", "").split())] for x in lines]

result = 0

for line in lines:
    differences = [line]

    done = False

    while not done:
        difference = []
        for i in range(len(differences[-1]) - 1):
            difference.append(differences[-1][i+1] - differences[-1][i])

        differences.append(difference)
        done = True
        for num in difference:
            if num != 0:
                done = False
                break

    differences.reverse()

    last_diff = 0
    for difference in differences:
        difference.insert(0, difference[0] - last_diff)
        last_diff = difference[0]
    result += differences[-1][0]

print(result)
