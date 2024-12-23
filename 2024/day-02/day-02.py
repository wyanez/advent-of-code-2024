#FILE_INPUT="2024/day-02/day-02-sample.in"
FILE_INPUT="2024/day-02/day-02.in"

def process(lines):
    data = []
    for line in lines:
        values = list(map(int,line.strip().split(' ')))
        data.append(values)
    return data
    
def part1_process_reports(values_reports):
    counter = 0
    for values in values_reports:
        if report_is_secure(values): counter += 1
    return counter

def report_is_secure(values_report):
    if abs(values_report[0] - values_report[1]) not in (1,2,3):
        return False
    
    previous = values_report[1]
    is_increasing = (values_report[1] - values_report[0]) > 0
    is_secure = True
    for i in range(2, len(values_report)):
        value = values_report[i]
        diff = abs(value - previous)
        if is_increasing:
            if (value <= previous) or (diff not in (1,2,3)):
                is_secure = False
                break
        else:
            if (value >= previous) or (diff not in (1,2,3)):
                is_secure = False
                break
        
        previous = value
    return is_secure

# Part 2 with Problem Dampener
def part2_process_reports(values_reports):
    counter = 0
    for values in values_reports:
        if report_is_secure_part2(values): counter += 1
    return counter

def report_is_secure_part2(values_report):
    if report_is_secure(values_report):
        return True
    for i in range(len(values_report)):
        values_report_modified = values_report[:i] + values_report[i+1:]
        if report_is_secure(values_report_modified):
            return True
    return False

if __name__=="__main__":
    with open(FILE_INPUT) as input_file:
        lines = input_file.readlines()
        data = process(lines)
        result = part1_process_reports(data)
        print(result)
        result = part2_process_reports(data)
        print(result)
