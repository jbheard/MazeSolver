from random import randint # 
import struct, sys 

'''
Create an N*M maze using randomized DFS algorithm
	n - number of rows in the maze
	m - number of columns in the maze
'''
def maze_gen(n, m):
	# Modify dimensions to guarantee odd n,m
	n, m = n+(1 - n%2), m+(1 - m%2)
	# All even row/column pairs are vertices (path)
	vertices = []
	for i in range(0, n, 2):
		for j in range(0, m, 2):
			vertices.append( (i,j) )
	# All other areas are edges (walls)
	edges = []
	for i in range(n):
		for j in range(1-i%2, m, 1 + (1-i%2)):
			edges.append( (i,j) )

	# select random vertex in maze
	v = vertices[ randint(0, len(vertices) - 1) ]
	DFS_maze(v, vertices, edges, [])
	maze = []
	
	# Create empty maze
	for i in range(n):
		maze.append( [0] * m )
	# Insert every remaining edge as a wall
	for pos in edges:
		maze[pos[0]][pos[1]] = 1
	return maze

'''
A recursive and random implementation of Depth-First-Search for maze generating
	curr - The current vertex
	vertices - The list of all vertices
	edges - The list of all edges
	visited - A list of all visited nodes
'''
def DFS_maze(curr, vertices, edges, visited=[]):
	if curr in visited:
		return
	# Mark current as visited
	visited.append(curr)
	# Find all neighbors of current
	nb = get_neighbors(curr, vertices)
	while len(nb) > 0:
		e = nb.pop( randint(0, len(nb) - 1) )
		if e not in visited:
			# Convert an edge to a vertex, in other words,
			# break down a wall to make a path
			tmp = get_edge(curr, e)
			edges.remove( tmp )
			DFS_maze(e, vertices, edges, visited)

'''
Returns all neighboring nodes of a given vertex
	v - The vertex to find neighbors for
	vertices - A list of vertices to check for neighors
'''
def get_neighbors(v, vertices):
	# Find all vertices exactly 2 cells away 
	# (only consider up/down, left/right)
	# TODO: Faster way to do this? (i.e. < theta(n))
	nb = []
	for e in vertices:
		a = abs(e[0] - v[0])
		b = abs(e[1] - v[1])
		if (a == 2 and b == 0) or (b == 2 and a == 0):
			nb.append(e)
	return nb

'''
returns the edge between two given vertices
	v1, v2 - The two vertices to find an edge between
'''
def get_edge(v1, v2):
	# Calculate the halfway point between two vertices
	return ( v1[0] + (v2[0] - v1[0]) // 2,  v1[1] + (v2[1] - v1[1]) // 2)

'''
Write a maze to a binary file
	maze - The maze to write
	fname - The name of the file to output
'''
def write_maze(maze, fname):
	# Lambda for flattening a 2D list from:
	# https://stackoverflow.com/a/952952/
	flatten = lambda l: [item for sublist in l for item in sublist]
	
	# Open the file
	file = open(fname, 'wb')
	
	maze_size = len(maze[0]) * len(maze)
	dim = [len(maze[0]), len(maze)]
	data = struct.pack('<'+'b'*maze_size, *flatten(maze))
	
	# Write the maze dimensions and data
	file.write(struct.pack('<ii', *dim))
	file.write(data)
	# Close the file
	file.close()

'''
Read a maze from a binary file
	fname - The file name to read
'''
def read_maze(fname):
	# Open maze and read dimensions of maze
	file = open(fname, 'rb')
	n, m = struct.unpack('<ii', file.read(8))
	
	# Read all raw data from file
	tmp = file.read(n*m*4)
	bytes_left = n*m*4 - len(tmp)
	raw_data = tmp
	while len(tmp) != 0:
		tmp = file.read(bytes_left)
		bytes_left -= len(tmp)
		raw_data += tmp
	file.close()

	# Unpack maze and convert from 1D to 2D array
	maze = struct.unpack('<' + 'b'*n*m, raw_data)
	maze = [ maze[i*n:i*n+m] for i in range(n) ]
	return maze

'''
Prints a given maze as an array of integers to a stream (default: sys.stdout)
	maze - The maze to print
	f - The stream to output to
'''
def print_maze(maze, f=sys.stdout):
	for r in range(len(maze)): # rows
		for c in range(len(maze[r])): # cols
			print(' %d' % maze[r][c] , end='', file=f)
		print() # Print newline between rows

# Main program to test functions
if __name__ == '__main__':
	# Get dimension and output file
	n = int(input("Enter N: "))
	fname = input("Enter filename for maze: ")
	# Generate the maze
	maze = maze_gen(n,n)
	# Test printing, reading, writing functions
	print_maze(maze)
	write_maze(maze, fname)
	maze = read_maze(fname)
	print("Read mazefrom file: ")
	print_maze(maze)

