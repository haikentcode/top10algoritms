def bfs( start, end, graph ):
	todo = [(start, [start])]
	while len( todo ):
		node, path = todo.pop( 0 )
		for next_node in graph[node]:
			if next_node in path:
				continue
			elif next_node == end:
				yield path + [next_node]
			else:
				todo.append( (next_node, path + [next_node]) )


if __name__ == '__main__':
	graph = { 'A': ['B','C'],
			  'B': ['D'],
			  'C': ['E'],
			  'D': ['E', 'F'],
			  'E': [] }
	[ print( x ) for x in bfs( 'A', 'F', graph ) ]
