from HW7_Student import *
import sys

def main():

	if (len(sys.argv) < 2):
		print("Please provide the input filepath as the argument")
		sys.exit()

	input_file = sys.argv[1]
	start_node = 0
	graph = {}
	node = 0

	#Reading and parsing the file
	with open(input_file, 'r') as file:
		start_node = int(file.readline())
		end_node = int(file.readline())
		for line in file:
			adjList = [int(neighbor) for neighbor in line.split()]
			graph[node] = adjList
			node += 1

	print("Number of nodes:" + str(len(graph.keys())))
	print("Start node: " + str(start_node) + " End node: " + str(end_node))

	#Get the path
	path = HW7_Student(start_node, end_node, graph)

	print(path)


if __name__ == '__main__':
	main()
