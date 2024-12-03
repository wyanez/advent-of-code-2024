import re
from functools import reduce

#FILE_INPUT="2024/day-03/day-03-sample.in"
FILE_INPUT="2024/day-03/day-03.in"

def process_input_part1(lines):
    input_line = "".join(lines)
    muls = re.findall(r"mul\(\d+,\d+\)", input_line)
    pairs_values = map(lambda mul : re.findall(r'\d+',mul), muls)
    pairs_values_int = list(map(lambda arr: (int(arr[0]), int(arr[1])), pairs_values))
    return pairs_values_int

def part1(lines):
    values = process_input_part1(lines)
    multiply_results = list(map(lambda item: item[0]*item[1],values))
    return reduce(lambda x, y: x + y, multiply_results)

if __name__=="__main__":
    with open(FILE_INPUT) as input_file:
        lines = input_file.readlines()
        result = part1(lines)
        print(result)
