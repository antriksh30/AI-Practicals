import heapq

def show_open_close(open_set, close_list, node_names):
    print("Open Set:", end=" ")
    for node in open_set:
        print(node_names[node], end=" ")
    print("\nClosed List:", end=" ")
    for node in close_list:
        print(node_names[node], end=" ")
    print()

def print_final_path(parent, start, dest, node_names):
    path = [dest]
    current = dest
    while current != start:
        current = parent[current]
        path.insert(0, current)
    print("Final Path:", ' -> '.join(node_names[i] for i in path))


def main():
    pq = []  # priority queue (f, node)
    node_names = ['S','B', 'C', 'D', 'E', 'F', 'G']

    open_set = set()
    close_list = []
    adj = [
        [(1, 4), (2, 3)],
        [(5, 5), (4, 12)],
        [(3, 7),(4, 10)],
        [(4, 2)],
        [(6, 5)],
        [(6, 16)],
        []
    ]

    heur = [14, 12, 11, 6, 4, 11, 0]

    vis = [False] * 7
    dest = 6

    g_values = [float('inf')] * 7
    g_values[0] = 0

    parent = [-1] * 7

    heapq.heappush(pq, (heur[0], 0))
    open_set.add(0)

    while pq:
        f_value, node = heapq.heappop(pq)
        vis[node] = True
        open_set.discard(node)
        print(f"\n{node_names[node]} > f:{f_value} g:{g_values[node]} h:{heur[node]}")
        if node == dest:
            show_open_close(open_set, close_list, node_names)
            print(f"{node_names[dest]} is the Destination, and the optimal distance is {g_values[node]}\n")
            print_final_path(parent, 0, dest, node_names)
            break
        for neighbor, weight in adj[node]:
            tentative_g_value = g_values[node] + weight
            if not vis[neighbor] and tentative_g_value < g_values[neighbor]:
                g_values[neighbor] = tentative_g_value
                if neighbor in open_set:
                    for i in range(len(pq)):
                        if pq[i][1] == neighbor:
                            pq[i] = (g_values[neighbor] + heur[neighbor], neighbor)
                            heapq.heapify(pq)
                            break
                else:
                    heapq.heappush(pq, (g_values[neighbor] + heur[neighbor], neighbor))
                open_set.add(neighbor)
                parent[neighbor] = node
        close_list.append(node)
        show_open_close(open_set, close_list, node_names)

if __name__ == "__main__":
    main()
