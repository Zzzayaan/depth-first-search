# Create an adjacency list
graph = {
	'A' : ['B', 'C'],
	'B' : ['D'],
	'C' : ['E', 'F'],
	'D' : [],
	'E' : ['G'],
	'F' : ['H'],
	'G' : ['H'],
	'H' : []
}

# Set contains visited vertices
visited = set()

# Passes values of the graph, visited vertices, and the starting vertex
def dfs(visited, graph, vertex):
	if vertex not in visited:
		print(vertex)
		visited.add(vertex) # Appends vertex into visited set
		for n in graph[vertex]: # dfs is called again for vertex neighbours
			dfs(visited, graph, n)

test = dfs(visited, graph, 'C')
print(test)

# Output:
# C
# E
# G
# H
# F
# None
