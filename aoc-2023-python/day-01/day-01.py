import re

with open("input.txt", "r") as file:
    lines = file.readlines()

sum = 0

words_to_numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                    "six": "6", "seven": "7", "eight": "8", "nine": "9"}


for line in lines:
    for word in words_to_numbers:
        line = line.replace(word, word + words_to_numbers[word] + word)
    digits = re.findall(r"\d", line)
    sum += int(digits[0] + digits[-1])

print(sum)
