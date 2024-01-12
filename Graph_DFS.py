graph = {
    "A" : ["B", "C", "D"],
    "B" : ["E"],
    "C" : ["E","F"],
    "D" : ["F"],
    "E" : ["G"],
    "F" : ["G"],
    "G" : []
}

visited = set()

def depth_first_search(visited,graph,node):
    if node not in visited:
        print(node, end = " ")

        for adjacent in graph[node]:
            depth_first_search(visited,graph,adjacent)


depth_first_search(visited,graph,"A")
            
# print(graph["C"])