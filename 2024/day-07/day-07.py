import re
from itertools import product

# FILE_INPUT="2024/day-07/day-07-sample.in"
FILE_INPUT="2024/day-07/day-07.in"

def is_solution(values, operation, target):
    result = values[0]
    #print(values, operation, target)
    for i in range(1,len(values)):
        if operation[i-1] == '+':
            result += values[i]
        elif operation[i-1] == '*':
            result *= values[i]
        elif operation[i-1] == '||':
            result = int(str(result) + str(values[i]))
    return result == target

def find_operation_to_target(values, ops):
    posible_operations = product(ops, repeat=len(values[1:])-1)
    for operation in posible_operations:
        if is_solution(values[1:], operation, values[0]):
            return operation
    return None

def part1(lines):
    total = 0
    for line in lines:
        values = list(map(int,re.findall(r'\d+', line.strip())))
        assert len(values)>2
        ops = find_operation_to_target(values, ['+','*'])
        if ops:
            # print(values, ops)
            total += values[0]
    return total
        
def part2(lines):
    total = 0
    for line in lines:
        values = list(map(int,re.findall(r'\d+', line.strip())))
        assert len(values)>2
        ops = find_operation_to_target(values, ['+','*'])
        if ops:
            # print(values, ops)
            total += values[0]
        else:
            ops = find_operation_to_target(values, ['+','*', '||'])
            if ops:
                print(values, ops)
                total += values[0]

    return total

if __name__=="__main__":
    with open(FILE_INPUT) as input_file:
        lines = input_file.readlines()
        result = part1(lines)
        print(result)
        result = part2(lines)
        print(result)
