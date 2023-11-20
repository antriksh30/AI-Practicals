import heapq

def show_open_close(open_list, close_list, node_names):
    print("Open List:", end=" ")
    for node in open_list:
        print(node_names[node], end=" ")
    print("\nClosed List:", end=" ")
    for node in close_list:
        print(node_names[node], end=" ")
    print()

def main():
    pq = []  # priority queue (heuristic, node)
    node_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    open_list = []
    close_list = []
    adj = [
        [(1, 11), (2, 14), (3, 7)],
        [(4, 15)],
        [(4, 8), (5, 10)],
        [(5, 25)],
        [(7, 9)],
        [(6, 20)],
        [],
        [(6, 10)]
    ]

    heur = [40,32,25,35,19,17,0,10]

    vis = [0] * 8
    dest = 6

    heapq.heappush(pq, (heur[0], 0))
    path = {0: [0,]}
    open_list.append(0)
    #best first search
    while pq:
        heuristic, node = heapq.heappop(pq)
        vis[node] = 1
        open_list.remove(node)
        close_list.append(node)
        print(f"\n{node_names[node]} > h:{heuristic}")
        if node == dest:
            show_open_close(open_list, close_list, node_names)
            distance = 0
            for i in range(len(path[node])-1):
                for neighbor, weight in adj[path[node][i]]:
                    if neighbor == path[node][i+1]:
                        distance += weight
            print(f"{node_names[node]} is the Destination, and the distance is {distance}\n")
            print("Final Path:", ' -> '.join(node_names[i] for i in path[node]))
            break
        for neighbor, _ in adj[node]:
            if vis[neighbor] == 0:
                if neighbor not in open_list:
                    heapq.heappush(pq, (heur[neighbor], neighbor))
                    open_list.append(neighbor)
                    path[neighbor] = path[node] + [neighbor]
        show_open_close(open_list, close_list, node_names)
        
if __name__ == "__main__":
    main()
