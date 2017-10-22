#Matheus E. Santana.
#22/10/2017.
#Implementation of the Depth-first search algorithm (DFS). 
#Based on the algorithm of the book Theory and Practice Algorithms 3ed - Cap 22.4. - Thomas H. Cormem.
#the input file must be passed by command line.


class Vertice():
	def	__init__(self):
		self.id = 0
		self.color = "WHITE"
		self.d = 0				#time of discovery.
		self.f = 0				#end time of discovery.
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
		self.vList = []			#List of vertex.
		self.archive = archive	#file referring to the vertices and their adjacent ones.
		self.createGraph()		#Initalize the graph.
		self.time = 0

	#Initalize the graph.		
	def createGraph(self):
		#Open the archive
		arc = open(self.archive, 'r')
		n = int(arc.readline())
		
		#Initializing all vertices. 
		for i in range(n):
			vertex = Vertice()	
			vertex.id = i
			self.vList.append(vertex)


		#Adding edge between vertices. 
		lines = arc.readlines()
		for line in lines:	
			index, neighbor = map(int, line.split('-'))

			self.vList[index].neighbors.append(self.vList[neighbor])
			self.vList[neighbor].neighbors.append(self.vList[index])


	#print list of vertices 		
	def printVList(self):
		for vertex in self.vList:
			print("Vertex:",vertex.id,"- Color:",vertex.color," time of discovery:", vertex.d, "- f:", vertex.f)

	#print list of vertices and their neighbors
	def printVListAdjacents(self):
		for vertex in self.vList:
			vertex.printNeighbors()
			print("\n")

	def dfs(self):
		for vertex in self.vList:
			if vertex.color == "WHITE":
				self.dfsVisit(vertex)

	def dfsVisit(self, vertex):
		self.time +=1			#time of discovery.
		vertex.d = self.time
		vertex.color = "GREY"	#coloring the processed vertex.
		#Searching deeper.
		for neighbor in vertex.neighbors:
			if neighbor.color == "WHITE":
				neighbor.predecessor = vertex
				self.dfsVisit(neighbor)
		vertex.color = "BLACK"
		self.time +=1			#end time of discovery.	
		vertex.f = self.time

	#sort vertex from graph by time of discovery.
	def sortD(self):
		self.vList.sort(key=lambda v: v.d)

arc = input()
graph = Graph(arc)	
graph.dfs()
graph.sortD()
graph.printVList()