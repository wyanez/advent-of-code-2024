import re
from functools import reduce

#FILE_INPUT="2024/day-03/day-03-sample2.in"
FILE_INPUT="2024/day-03/day-03.in"

def process_input_part1(lines):
    input_line = "".join(lines)
    muls = re.findall(r"mul\(\d+,\d+\)", input_line)
    return muls

def part1(lines):
    muls_list = process_input_part1(lines)
    values = get_mul_operands(muls_list)
    return resolve_multiply(values)

def get_mul_operands(muls_list):
    pairs_values = map(lambda mul : re.findall(r'\d+',mul), muls_list)
    pairs_values_int = list(map(lambda arr: (int(arr[0]), int(arr[1])), pairs_values))
    return pairs_values_int

def resolve_multiply(values):
    multiply_results = list(map(lambda item: item[0]*item[1],values))
    return reduce(lambda x, y: x + y, multiply_results)

def process_input_part2(lines):
    input_line = "".join(lines)
    result = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_line)
    ok = True
    muls = []
    for item in result:
        if ok and item[:4] == 'mul(':
            muls.append(item)
        elif item == "do()":
            ok = True
        elif item == "don't()":
            ok = False
    return muls

def part2(lines):
    muls_list = process_input_part2(lines)
    values = get_mul_operands(muls_list)
    return resolve_multiply(values)

if __name__=="__main__":
    with open(FILE_INPUT) as input_file:
        lines = input_file.readlines()
        result = part1(lines)
        print(result)
        result = part2(lines)
        print(result)
