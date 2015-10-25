import sys

# read in from stdin, run by doing:
# > cat data.tx | python pq5.py
data = sys.stdin.readlines()

# data structures to hold adjacency list
GRAPH = {}     # {node: [outgoing_edges]}
NODES = []
DISTANCES = {} # {(node,node): distance}

for data_line in data:
	line = data_line.split('\t')
	del line[len(line)-1]
	node = line.pop(0)
	NODES.append(node)
	for pair in line:
		other_node, dist = pair.split(',')
		if node not in GRAPH:
			GRAPH[node] = [other_node]
		else:
			GRAPH[node].append(other_node)
		DISTANCES[(node, other_node)] = int(dist)

nodes_processed = ['1']
shortest_path = {'1': 0} # {node: shortest_path_distance}

while len(nodes_processed) < len(NODES):
	outgoing_edges = [] # holds tuples representing edges: (from, to)
	for node in nodes_processed:
		for edge in GRAPH[node]:
			if edge not in nodes_processed:
				outgoing_edges.append((node, edge))
	min_dist = None
	next_node = None
	# edge[0] = from node
	# edge[1] = to node
	for edge in outgoing_edges:
		if edge[1] not in nodes_processed: # remove this if?
			new_dist = shortest_path[edge[0]] + DISTANCES[(edge[0], edge[1])]
			if min_dist is None:
				min_dist = new_dist
				next_node = edge[1]
			elif new_dist < min_dist:
				min_dist = new_dist
				next_node = edge[1]
	nodes_processed.append(next_node)
	shortest_path[next_node] = min_dist

print shortest_path
