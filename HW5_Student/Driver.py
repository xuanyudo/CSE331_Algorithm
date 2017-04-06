from HW5_Student import *
import sys

def main():

	if (len(sys.argv) < 2):
		print("Please provide the input filepath as the argument")
		sys.exit()

	input_file = sys.argv[1]
	graph = {}
	node = 0

	#Reading and parsing the file
	with open(input_file, 'r') as file:
		for line in file:
			adjList = [int(neighbor) for neighbor in line.split()]
			graph[node] = adjList
			node += 1

	print("Number of nodes:" + str(len(graph.keys())))

	#Get the cycle
	cycle = HW5_Student(graph)

	print(cycle)


if __name__ == '__main__':
	main()
