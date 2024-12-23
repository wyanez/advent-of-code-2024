FILE_INPUT="2024/day-23/day-23-sample.in"
#FILE_INPUT="2024/day-23/day-23.in"

class Graph:
    def __init__(self, directed = False):
        self.ady_list = {}
        self.directed = directed
    
    def add_edge(self, vertex1, vertex2):
        v1_ady = self.ady_list.get(vertex1,[])
        v1_ady.append(vertex2)
        self.ady_list[vertex1] = v1_ady
        if not self.directed:
            v2_ady = self.ady_list.get(vertex2,[])
            v2_ady.append(vertex1)
            self.ady_list[vertex2] = v2_ady
    
    def get_nodes(self):
        return self.ady_list.keys()
    
    def get_ady_list(self, v: str):
        return self.ady_list[v]

    def is_connected(self, v1, v2):
        v1_ady = self.ady_list.get(v1,[])
        return v2 in v1_ady
    
    def print(self):
        for node in self.ady_list.keys():
            print(node, self.ady_list[node]) 


def build_graph(list_nodes):
    g = Graph()
    for node_pair in list_nodes:
        g.add_edge(node_pair[0], node_pair[1])
    return g

def build_set_of_three_nodes(graph: Graph ) -> None :
    result = set()
    for node1 in graph.get_nodes():
        list_ady1 = graph.get_ady_list(node1)
        #print(node1, list_ady1)
        for node2 in list_ady1:
             list_ady2 = graph.get_ady_list(node2)
             for node3 in list_ady2:
                 if graph.is_connected(node1, node3):
                     aux = [ node1, node2, node3]
                     aux.sort()
                     result.add(",".join(aux))
    
    list_result = list(result)
    list_result.sort()
    print(list_result)
    print(len(result))
    node_start_with_t = filter(lambda s: any(map(lambda node: node[0]=='t', s.split(','))), list_result)
    return list(node_start_with_t)

def part1(graph: Graph) -> None:
    result = build_set_of_three_nodes(graph)
    print(result)
    print(len(result))

def process(lines):
    result = map(lambda line: line.strip().split('-'), lines) 
    return list(result)

if __name__=="__main__":
    with open(FILE_INPUT) as input_file:
        lines = input_file.readlines()
        list_nodes = process(lines)
        graph = build_graph(list_nodes)
        part1(graph)
        
        