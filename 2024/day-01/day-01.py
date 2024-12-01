import re

#FILE_INPUT="2024/day-01/day-01-sample.in"
FILE_INPUT="2024/day-01/day-01.in"

def calculate_distance(list1, list2):
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
    return distance

def calculate_similarity_score(list1, list2):
    score = 0
    for value in list1:
        score += value * list2.count(value)
    return score

def process(lines):
    list1 = []
    list2 = []
    for line in lines:
        values = list(map(int,re.findall(r'\d+', line)))
        list1.append(values[0])
        list2.append(values[1])
    assert len(list1) == len(list2)
    return list1, list2


def part1(lines):
    list1, list2 = process(lines)
    list1.sort()
    list2.sort()
    return calculate_distance(list1, list2)

def part2(lines):
    list1, list2 = process(lines)
    return calculate_similarity_score(list1, list2)

if __name__=="__main__":
    with open(FILE_INPUT) as input_file:
        lines = input_file.readlines()
        result = part1(lines)
        print(result)
        result = part2(lines)
        print(result)

