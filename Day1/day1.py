import sys
sys.path.append('c:/Users/giova/OneDrive/Documents/GitHub/AdventOfCode2024')
from helper import read_txt_file, split_input_into_lists

# obtain input
input_filename = "puzzle_input1.txt"
input_foldername = "Day1"
input_txt = read_txt_file(input_foldername, input_filename)

# parse input into two lists
parsed_input = split_input_into_lists(input_txt)
list1 = parsed_input[0]
list2 = parsed_input[1]

def part1():
    list1.sort()
    list2.sort()

    distance = 0
    for i in range(len(list1)):
        distance += abs(int(list1[i]) - int(list2[i]))

    return distance

def part2():
    similarity_score = 0
    for i in list1:
        similarity_score += int(i) * list2.count(i)

    return similarity_score


print(part1())
print(part2())

