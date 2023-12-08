from collections import Counter

with open("input.txt", "r") as file:
    lines = file.readlines()

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pairs = []
pair = []
high_card = []

for line in lines:
    split = line.split()
    hand = (split[0], split[1])
    counter = Counter(hand[0])
    max_count = max(counter.values())

    temp = hand[0].replace("J", "")
    counter = Counter(temp)
    if len(temp) != 0:
        max_count = max(counter.values()) + hand[0].count("J")
    else:
        max_count = hand[0].count("J")

    # normal card handling
    if max_count == 5:
        five_of_a_kind.append(hand)
    elif max_count == 4:
        four_of_a_kind.append(hand)
    elif max_count == 3:
        if len(counter) == 2:
            full_house.append(hand)
        else:
            three_of_a_kind.append(hand)
    elif max_count == 2:
        if len(counter) == 3:
            two_pairs.append(hand)
        else:
            pair.append(hand)
    else:
        high_card.append(hand)

# Sort the lists
sort_order = {"A": 14, "K": 13, "Q": 12, "T": 10,
              "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}


def sort_key(hand):
    return [sort_order[card] for card in hand[0]]


five_of_a_kind.sort(key=sort_key, reverse=True)
four_of_a_kind.sort(key=sort_key, reverse=True)
full_house.sort(key=sort_key, reverse=True)
three_of_a_kind.sort(key=sort_key, reverse=True)
two_pairs.sort(key=sort_key, reverse=True)
pair.sort(key=sort_key, reverse=True)
high_card.sort(key=sort_key, reverse=True)

sorted_hands = five_of_a_kind + four_of_a_kind + \
    full_house + three_of_a_kind + two_pairs + pair + high_card

sorted_hands.reverse()

sum = 0

for i in range(len(sorted_hands)):
    sum += (i + 1) * int(sorted_hands[i][1])


print(sum)
