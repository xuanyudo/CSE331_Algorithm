from heapq import heappush,heappop

def HW10_Student(origin, outgoing_edges, incoming_edges):
	answer = [1000000000]*len(outgoing_edges)
	answer[origin]=0
	heap = []
	heappush(heap,(0,origin))
	while len(heap)!=0:
		cost,node = heappop(heap)
		for item in outgoing_edges[node]:
			fcost=outgoing_edges[node][item]+cost
			if answer[item]>fcost:
				answer[item]= fcost
				heappush(heap,(fcost,item))

	return answer
