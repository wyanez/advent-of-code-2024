FILE_INPUT="2024/day-06/day-06-sample.in"
FILE_INPUT="2024/day-06/day-06.in"

class MapPuzzle:

    def __init__(self, lines):
        self.guard_moves = { 
            '^': ((-1,0),'>'), 
            '>': ((0,1),'v'), 
            '<': ((0,-1),'^'),
            'v': ((1,0),'<')
        }
        self.current_guard_icon = '^'
        self._initialize_map(lines)
        # print(self._current_guard_move())
        
    def _current_guard_move(self):
        return self.guard_moves[self.current_guard_icon]

    def _initialize_map(self, lines):
        self.data = []
        for line in lines:
            self.data.append(list(line.strip()))
            if "^" in line:
                self.guard_position = {'row': len(self.data) - 1, 
                                       'col':line.index('^')}
        self.dimensions = (len(self.data), len(self.data[0]))
        #self.print_map()
    
    def print_map(self):
        for line in self.data:
            print("".join(line))
        print(self.guard_position)        
        print(self.dimensions)

    
    def is_obstacle(self, row, col):
        return self.data[row][col]=='#' or self.data[row][col]=='O'
    
    def start_tour(self):
        end_tour = False
        delta_row = self._current_guard_move()[0][0]
        delta_col = self._current_guard_move()[0][1]
        row = self.guard_position['row'] + delta_row
        col = self.guard_position['col'] + delta_col
        counter_walk = 1
        counter_cycle = 0
        last_position_cycle = None
        while 0 <= row <self.dimensions[0] and 0 <= col < self.dimensions[1]:
            last_visited = self.data[self.guard_position['row']][self.guard_position['col']]
            self.data[self.guard_position['row']][self.guard_position['col']] = 'X'
            self.guard_position['col'] = col
            self.guard_position['row'] = row
            if self.data[row][col] == 'X' and last_visited == 'X' :
                #print(f"***OJO X in ({row},{col}) -> {counter_walk}***")
                if counter_cycle == 0:
                    counter_cycle = 1
                    last_position_cycle = (row,col)
                else:
                    counter_cycle += 1    
                    if row == last_position_cycle[0] and col == last_position_cycle[1]:
                        #print(f"** Cycle in {last_position_cycle} -> {counter_cycle}")
                        break
            if self.data[row][col]=='.':
                counter_cycle = 0
                last_position_cycle = None
                self.data[row][col] = self.current_guard_icon 
                counter_walk += 1
            
            if 0 <= row + delta_row < self.dimensions[0] and 0 <= col + delta_col < self.dimensions[1] and self.is_obstacle(row + delta_row, col + delta_col):
                self.current_guard_icon = self._current_guard_move()[1]
                #print(self.current_guard_icon)
                #print(self._current_guard_move())
                delta_row = self._current_guard_move()[0][0]
                delta_col = self._current_guard_move()[0][1]
                
            row += delta_row
            col += delta_col    
        
        #self.print_map()
        if counter_cycle>0:
            return -1
        return counter_walk

    def get_element_at(self, row, col):
        return self.data[row][col]

    def set_obstacle(self,row, col):
        self.data[row][col] = 'O'

def part1(lines):
    puzzle = MapPuzzle(lines)
    result = puzzle.start_tour()
    print(result)
        
def part2(lines):
    rows = len(lines)
    cols = len(lines[0].strip())
    #print(rows,cols)
    counter_cicles = 0
    for i in range(rows):
        for j in range(cols):
            puzzle = MapPuzzle(lines)
            if puzzle.get_element_at(i, j):
                puzzle.set_obstacle(i, j)
                result = puzzle.start_tour()
                #print(result)
                if result == -1:
                    #print(f"obstacle({i},{j})")
                    #puzzle.print_map()
                    counter_cicles += 1
    print(counter_cicles)
            

if __name__=="__main__":
    with open(FILE_INPUT) as input_file:
        lines = input_file.readlines()
        part1(lines)
        part2(lines)
