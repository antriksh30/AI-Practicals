# AO* algorithm
def Cost(H, condition, weight=1):
    cost = {}
    
    if 'AND' in condition:
        AND_nodes = condition['AND']
        Path_A = 'AND'.join(AND_nodes)
        PathA = sum([H[node] + weight for node in AND_nodes])
        cost[Path_A] = PathA
        
    if 'OR' in condition:
        OR_nodes = condition['OR']
        for node in OR_nodes:
            Path_B = node
            PathB = H[node] + weight
            cost[Path_B] = PathB
    
    return cost

def update_cost(H, Conditions, weight=1):
    Main_nodes = list(Conditions.keys())
    Main_nodes.reverse()
    least_cost = {}
    
    for key in Main_nodes:
        condition = Conditions[key]
        c = Cost(H, condition, weight)
        H[key] = min(c.values())
        least_cost[key] = c
    
    return least_cost
def shortest_path(Start, Updated_cost, H, Path={}):
    
    if Start in Updated_cost.keys():
        Min_cost = H[Start]
        key_value_pairs = list(Updated_cost[Start].items())
        for key, value in key_value_pairs:
            if value == Min_cost:
                Path[Start] = key
                Next = key.split('AND')
                for node in Next:
                    shortest_path(node, Updated_cost, H) 
    
    return Path

H = {
    'A': 3,
    'B': 7,
    'C': 1,
    'D': 6,
    'E': 8,
    'F': 9,
    'G': 4,
    'H': 0,
    'I': 0,
    'J': 0
}

Conditions = {
    'A': {'OR': ['B'], 'AND': ['C', 'D']},
    'B': {'OR': ['E', 'F']},
    'C': {'OR': ['G'], 'AND': ['H', 'I']},
    'D': {'OR': ['J']}
}

weight = 2

print('Updated Cost:')
Updated_cost = update_cost(H, Conditions, weight=2)
print(Updated_cost)

print('Shortest Path:')
shortest_path_str = shortest_path('A', Updated_cost, H)
for key, value in shortest_path_str.items():
    print(key, '<-', value)
