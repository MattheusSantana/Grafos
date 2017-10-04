V_ENABLE = 1
V_DISABLE = 0

class Vertex(object):
	def __init__(self):
		self.id = 0
		self.color = None
		self.status = V_ENABLE
		self.degree = 0
		self.label = ""
		self.neighbors = []
		self.ecNumber = 0


	def printNeighbors(self):
		print("%d  {"%(self.id), end="")
		for neighbor in self.neighbors:
			print("----> %d"%( neighbor.id), end=" ")

		print("}")	
	


class Graph(object):
	def __init__(self):
		self.n = 0			# Number of vertices 
		self.ocurrences = 0 # Number of ocurrences
		self.maxN = 0		# Max number of vertices
		self.maxColor = 0	# Max number of colors
		self.vList = []		# List of vertices
		self.topologicalOrder = []


	def printVertices(self):
		for vertex in self.vList:
			print(vertex.id, vertex.color, vertex.label)	
	
	def printAdjacents(self):
		for vertex in self.vList:
			vertex.printNeighbors()	

	def CreateMotif(self, archive):
		arc = open(archive, 'r')
		entry = arc.readline()
		numberVertices, maxColor = entry.split(',')
		self.maxN = int(numberVertices)
		self.maxColor = int(maxColor)

		for i in range(self.maxN):
			line = arc.readline()
			index, color = line.split(':')
			vertex = Vertex()
			vertex.id = int(index)
			vertex.color = int(color)
			self.vList.append(vertex)
			self.n += 1
		
		lines = arc.readlines()
		
		for line in lines:
			index, neighbor = line.split('-')

			#Adding Edges between the vertices
			self.vList[int(index)].neighbors.append(self.vList[int(neighbor)])
			self.vList[int(neighbor)].neighbors.append(self.vList[int(index)])	
		arc.close()	

	#the final order of dfs is reverse.	
	def dfs(self):
		for vertex in self.vList:
			vertex.status = V_ENABLE
		
		for vertex in self.vList:
			if(vertex.status):
				self.dfsVisit(vertex)

		#self.topologicalOrder.reverse()			

	def dfsVisit(self, vertex):
		#Pintando o vértice de cinza.
		vertex.status = V_DISABLE
	
		#Navegando pelos vertices v adj[v, u]
		for neighbor in vertex.neighbors:
			#Caso o vértice não tenha sido visitado ainda, chame a função de forma recursiva, navegando mais profundamente no grafo.
			if(neighbor.status):
				self.dfsVisit(neighbor)

		#Adicionando o vértice já processado em uma lista.
		self.topologicalOrder.append(vertex)


	def TCG(self, motif):
		for i in range(len(motif.topologicalOrder)):
			v = motif.topologicalOrder[i]
			A = []

			for a in self.vList:
				if a.status == V_ENABLE and a.color == v.color:
					A.append(a)
					
			w = v.neighbors[0]
			if(i == len(motif.topologicalOrder)-1):
				if(len(A) == 0):
					print("No occurrences")
					return;
				else:
					print("The motif occurs in the graph")
					return;	
		
			for b in self.vList:
				if b.status == V_ENABLE and b.color == w.color:
					if self.adjTo(b,v) == 1:
						self.vList[b.id].status = V_DISABLE

			for a in self.vList:
				if a.status == V_ENABLE and a.color == v.color:
					self.vList[a.id].status = V_DISABLE			

	def adjTo(self, x, w):
		for vertex in x.neighbors:
			if(vertex.status == 1 and vertex.color == w.color):
				return 0
		return 1					

#Initializing graph that be populated.
graph = Graph()	

#Open archive reference to graph
arq = open('graph-e.coli_BioCyc_K12-clean.txt', 'r')

#reading number of vertices and number maxime of colors
firstLine = arq.readline()

verticesNumber, colorsNumber = firstLine.split(',')
graph.maxN = int(verticesNumber)
graph.maxColor = int(colorsNumber)

#Initializing vertices
for i in range(graph.maxN):
	line = arq.readline()
	string1, string2 = line.split()
	index, color = string1.split(':')
	label, ec = string2.split(':')

	vertex = Vertex()
	vertex.id = int(index)
	vertex.color = int(color)
	vertex.label = label
	vertex.ecNumber = ec

	graph.vList.append(vertex)
	graph.n += 1

#Adding neighbors of the vertices
for line in arq.readlines():
	index, adj = line.split('-')
	
	graph.vList[int(index)].neighbors.append(graph.vList[int(adj)])
	graph.vList[int(adj)].neighbors.append(graph.vList[int(index)])


arq.close()	
motif = Graph()

motif.CreateMotif("motif-600.txt")

motif.dfs()

graph.TCG(motif)
