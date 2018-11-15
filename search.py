from stack import Stack
from queue import Queue
import copy

# Constant for paths in maze
PATH = 0

'''
Solves a maze via Breadth-First Search
	maze  - The maze to use
	start - The start point in the maze as a coordinate (x,y)
	goal  - The end point in the maze as a coordinate (x,y)
returns: the path from start to goal as a linked list of coordinates
	backwards from the goal in the format (x,y,parent)
	or None if there is no solution
'''
def BFS(maze, start, goal):
	maze = copy.deepcopy(maze) # Create a copy so we can modify it
	q = Queue() # Queue for traversing breadth-first
	start = (start[0], start[1], None) # Change to mode with parent
	q.insert(start) # Init queue with the start node
	while not q.is_empty():
		# Get current node
		x, y, parent = q.remove()
		# Goal test
		if x == goal[0] and y == goal[1]: return (x,y,parent)
		# Check all vertical and horizontal neighbors
		for x0,y0 in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
			# Out of bounds checks
			if x0 < 0 or y0 < 0: continue
			if x0 == len(maze) or y0 == len(maze[0]): continue
			# Expand the node
			if maze[x0][y0] == PATH:
				q.insert((x0,y0, (x,y,parent)))
				maze[x0][y0] = -1 # Show that this node has been expanded
	return None

'''
Solves a maze via Depth-First Search
	maze  - The maze to use
	start - The start point in the maze as a coordinate (x,y)
	goal  - The end point in the maze as a coordinate (x,y)
returns: the path from start to goal as a linked list of coordinates
	backwards from the goal in the format (x,y,parent)
	or None if there is no solution
'''
def DFS(maze, start, goal):
	maze = copy.deepcopy(maze) # Create a copy so we can modify it
	s = Stack() # Stack for traversing depth-first
	start = (start[0], start[1], None) # Change to mode with parent
	s.push(start) # Init stack with the start node
	while not q.is_empty():
		# Get current node
		x, y, parent = s.pop()
		# Goal test
		if x == goal[0] and y == goal[1]: return (x,y,parent)
		# Check all vertical and horizontal neighbors
		for x0,y0 in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
			# Out of bounds checks
			if x0 < 0 or y0 < 0: continue
			if x0 == len(maze) or y0 == len(maze[0]): continue
			# Expand the node
			if maze[x0][y0] == PATH:
				s.push((x0,y0, (x,y,parent)))
				maze[x0][y0] = -1 # Show that this node has been expanded
	return None

