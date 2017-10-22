#Matheus E. Santana
#22/10/2017
#Implementation of the Breadth-first search algorithm (BFS). 
#Based on the algorithm of the book Theory and Practice Algorithms 3ed - Cap 22.2. - Thomas H. Cormem
#the input file must be passed by command line


class Vertice():
	def	__init__(self):
		self.id = 0
		self.color = "WHITE"
		self.degree = -1
		self.predecessor = None
		self.neighbors = []

	#Print all vertex neighbors 	
	def printNeighbors(self):
		print(self.id, "-> {", end="")
		for neighbor in self.neighbors:
			print(neighbor.id, end=" ")	
		print("}", end="")	

class Graph():
	def __init__(self, archive):
		self.vList = []			#List of vertex
		self.archive = archive	#file referring to the vertices and their adjacent ones
		self.createGraph()		#Initalize the graph.


	#Initalize the graph.		
	def createGraph(self):
		#Open the archive
		arc = open(self.archive, 'r')
		n = int(arc.readline())
		
		#Initializing all vertices 
		for i in range(n):
			vertex = Vertice()	
			vertex.id = i
			self.vList.append(vertex)


		#Adding edge between vertices 
		lines = arc.readlines()
		for line in lines:	
			index, neighbor = map(int, line.split('-'))

			self.vList[index].neighbors.append(self.vList[neighbor])
			self.vList[neighbor].neighbors.append(self.vList[index])


	#print list of vertices 		
	def printVList(self):
		for vertex in self.vList:
			print("Vertex:",vertex.id,"- Color:",vertex.color,"- Degree:", vertex.degree)

	#print list of vertices and their neighbors
	def printVListAdjacents(self):
		for vertex in self.vList:
			vertex.printNeighbors()
			print("\n")

	def bfs(self):
		vertex = self.vList[0]
		vertex.color = "GREY"
		vertex.degree = 0
		queue = []
		queue.append(vertex)
		while queue:
			vertex = queue.pop(0)
			for neighbor in vertex.neighbors:
				if neighbor.color == "WHITE":
					neighbor.color = "GREY"
					neighbor.degree = vertex.degree + 1
					neighbor.predecessor = vertex
					queue.append(neighbor)
			vertex.color = "BLACK"		

	#sort vertex from graph by order of degree.		
	def sortDegree(self):
		self.vList.sort(key=lambda v: v.degree)

arc = input()
graph = Graph(arc)	
graph.bfs()
graph.sortDegree()
graph.printVList()