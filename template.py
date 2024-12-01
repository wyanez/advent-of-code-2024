FILE_INPUT="2024/day-XX/day-XX-sample.in"

def process(lines):
    for line in lines:
        # values = line.strip().split(' ')
        # list of numbers
        # values = list(map(int,re.findall(r'\d+', line)))
        pass

if __name__=="__main__":
    with open(FILE_INPUT) as input_file:
        lines = input_file.readlines()
        process(lines)
