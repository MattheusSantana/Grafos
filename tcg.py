V_ENABLE = 1
V_DISABLE = 0

class Vertex(object):
	def __init__(self):
		self.id = 0
		self.color = None
		self.status = V_ENABLE
		self.degree = 0
		self.label = ""			
		self.neighbors = []		#Adjacents vertices
		self.ecNumber = 0 		#not being used for now
		self.brand = V_ENABLE	#it may be that you participate in a motif
		self.level = 0			#discovery time of DFS 

	def printNeighbors(self):
		print("%d  {"%(self.id), end="")
		for neighbor in self.neighbors:
			print("----> %d"%( neighbor.id), end=" ")

		print("}")	
	


class Graph(object):
	def __init__(self):
		self.n = 0	        # Number of vertices 
		self.ocurrences = 0 # Number of ocurrences
		self.maxN = 0		# Max number of vertices
		self.maxColor = 0	# Max number of colors
		self.vList = []		# List of vertices
		self.topologicalOrder = []
		self.level = 0
		
		self.map = []
	def printVertices(self):
		for vertex in self.vList:
			print(vertex.id, vertex.color, vertex.label)	
	
	def printAdjacents(self):
		for vertex in self.vList:
			vertex.printNeighbors()	

	#creates a graph referring to the input file		
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
	#A Simple depth-first search
	def dfs(self):
		for vertex in self.vList:
			vertex.status = V_ENABLE
		
		for vertex in self.vList:
			if(vertex.status):
				self.dfsVisit(vertex)

	#2 step of depth-first search	
	def dfsVisit(self, vertex):
		vertex.status = V_DISABLE
	
		for neighbor in vertex.neighbors:
			if(neighbor.status):
				self.dfsVisit(neighbor)

		vertex.level = self.level		
		self.level +=1
		self.topologicalOrder.append(vertex)

	#search for an instance of the motif in the graph
	def TCG(self, motif):
		for i in range(len(motif.topologicalOrder)):
			v = motif.topologicalOrder[i]
			A = []
			w = None
			
			for a in self.vList:
				if a.status == V_ENABLE and a.color == v.color:
					A.append(a)
			
			w = v.neighbors[0]

			#selecting neighbor that has a level greater than vertex v to maintain the order of dfs.
			for neighbor in v.neighbors:
				if(neighbor.level > v.level):	
					w = neighbor
					break
			

			if(i == len(motif.topologicalOrder)-1):
				self.map.append(v)
				if(len(A) == 0):
					print("No occurrences")
					return;
				else:
					print("The motif occurs in the graph")
					return;	

			self.map.append(w)
		
			for b in self.vList:
				if b.status == V_ENABLE and b.color == w.color:
					if self.adjTo(b,v) == 1:
						self.vList[b.id].brand = V_DISABLE
						self.vList[b.id].status = V_DISABLE

			for a in self.vList:
				if a.status == V_ENABLE and a.color == v.color:
					self.vList[a.id].status = V_DISABLE			
	#It says if two vertices are adjacent
	def adjTo(self, x, w):
		for vertex in x.neighbors:
			if(vertex.status == 1 and vertex.color == w.color):
				return 0
		return 1	

	def ocurrence(self, array, motif):
		aux = self.map[-1]

		#Obtaining leaf belonging to a motif
		for v in self.vList:
			if v.brand == V_ENABLE and v.color == aux.color:
				#Adding vertex on ultimate position of array.
				array[-1] = v
				break
		for i in range(len(self.map)-2, -1, -1):
			
			index =  self.map[i].level
			
			vertex = array[index]
			color = motif.topologicalOrder[i].color
			
			
			for neighbor in vertex.neighbors:
				if neighbor.brand == V_ENABLE and neighbor.color == color:
					array[i] = neighbor
					break	

		#Print the ocurrence
		print("Ocurrence:", end="")
		for i in range(0, len(array), 1):
			print(array[i].id, end=" ")
						
#Initializing graph that be populated.
graph = Graph()	

#Open archive reference to graph
arq = open('graph-2.txt', 'r')

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

motif.CreateMotif("motif-2.txt")

motif.dfs()
print("Ordem topologica")
for x  in motif.topologicalOrder:
	print(x.id, end=" - ")
print("\n------------------")
graph.TCG(motif)

#save an occurrence.
v = [None] * len(motif.vList)
graph.ocurrence(v, motif)
