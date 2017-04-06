def readFromFile(inputFile):

	rallies = []

	with open(inputFile, 'r') as file:

		numberOfRallies = int(file.readline())
		
		for i in range(0, numberOfRallies):
			durationAndDeadline = file.readline().split()
			rallies.append((int(durationAndDeadline[0]), int(durationAndDeadline[1])))

	return rallies
