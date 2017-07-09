#Conjuntos Fortemente COnexos
#Programador: Matheus E. Santana
#09/07/2017
#Este programa calcula e imprime os conjuntos fortemente conexos de um grafo. Efetuando a busca em profundidade,
#Calculando a matriz transposta ao grafo e refazendo a busca em profundidade mas agora em órdem decrescente do tempo de término f[u].   
#A implementação foi baseada no algoritmo do livro Algoritmos Teoria e Prática 2ed - Cap 22.5. - Thomas H. Cormem

class Grafo():
	def __init__(self):
		self.qtdVertices = 0	 	# Armazena a quantidade de vértices do grafo.	
		self.vertices = []			# Armazena os vértices.
		self.tempo = 0				# Contador de tempo de início e término de análise do vértice. 
		self.ordemTopologica = [] 	# Armazena os vértices na ordem da dfs.
	
	def setQtdVertices(self, qtd):
		self.qtdVertices = qtd	

	def getQtdVertices(self):
		return self.qtdVertices

	def setVerticesEmNivel(self, no):
		self.verticesEmNivel.append(no)	

	def imprimeGrafo(self):
		for i in range(self.qtdVertices):
			print("%d" %(self.vertices[i].getInfo()))

	# Busca em Profundidade.
	def dfs(self):
		#Navegando por todos os vértices do grafo.
		for i in range(self.qtdVertices):
			#Pintando vertice de branco.
			self.vertices[i].setCor("Branco")
			#Apontando predecessor do nó como nulo.
			self.vertices[i].setPredecessor(None)
			#Inicializando o tempo 
			self.tempo = 0
		#Navegando pelos vértices brancos do grafo.	
		for i in range(self.getQtdVertices()):
			if(self.vertices[i].getCor() == "Branco"):
				self.dfsVisit(self.vertices[i])
						
	# Visitando os nós na busca em profundidade			
	def dfsVisit(self, vertice):
		#Pintando o vértice de cinza.
		vertice.setCor("Cinza")
		self.tempo = self.tempo + 1
		vertice.setD(self.tempo)
	
		#Navegando pelos vertices v adj[v, u]
		for i in range(vertice.getQtdAdjacentes()):
			#Caso o vértice não tenha sido visitado ainda, chame a função de forma recursiva, navegando mais profundamente no grafo.
			if(vertice.adjacentes[i].getCor() == "Branco"):
				vertice.adjacentes[i].setPredecessor(vertice)
				self.dfsVisit(vertice.adjacentes[i])

		#Finalizando a visita do vértice.		
		vertice.setCor("Preto")
		self.tempo = self.tempo + 1
		vertice.setF(self.tempo)
		#Adicionando o vértice já processado em uma lista.
		self.setOrdemTopologica(vertice)			


	# Calcula e imprime os conjuntos de componentes fortemente conexos.
	def stronglyConnectedComponents(self):
		#Navegando por todos os vértices do grafo.
		for i in range(self.qtdVertices):
			#Pintando vertice de branco.
			self.vertices[i].setCor("Branco")
			#Apontando predecessor do nó como nulo.
			self.vertices[i].setPredecessor(None)
			#Inicializando o tempo 
			self.tempo = 0
		#efetuando busca em profundidade segundo a ordem topológica decrescente.	
		for i in range(self.getQtdVertices()):
			if(self.ordemTopologica[i].getCor() == "Branco"):
				self.dfsVisit(self.ordemTopologica[i])	


	#Adiciona um vértice já processado pela DFS.	
	def setOrdemTopologica(self, vertice):
		self.ordemTopologica.append(vertice)

	#Imprime os vértices do grafo em ordem topológica, da menor para a maior prioridade.	
	def imprimeOrdemTopologica(self):
		self.ordemTopologica.reverse()
		for i in range(self.qtdVertices):
			self.ordemTopologica[i].getTempo()	

	#Imprime conjuntos de componentes fortemente conexos.	
	def imprimeConjuntosFortementeConexos(self):
		self.ordemTopologica.reverse()
		for i in range(self.qtdVertices):
			if(self.ordemTopologica[i].predecessor == None):
				print("---Conjunto---")
				self.ordemTopologica[i].getTempo()	
			else:
				self.ordemTopologica[i].getTempo()	
		


class Vertice():
	def __init__(self):
		self.info = None		# Armazena o valor do vertice.
		self.distancia = 0		# Distância até um determinado vértice.
		self.cor = None 		# Iniciando vértice como não marcado.
		self.adjacentes = []	# Recebe vértices adjacentes.
		self.qtdAdjacentes = 0	# Quantidade de arestas do vértice
		self.proximo = None		# Ponteiro para o próximo vértice na fila.
		self.d = 0				# Tempo que levou para ser descoberto
		self.f = 0				# Tempo que levou para examinar a lista de adjacentes.
		self.predecessor = None # Mantém o nó antecessor.

	def setInfo(self, info):
		self.info = info

	def getInfo(self):
		return self.info	

	def setDistancia(self, distancia):
		self.distancia = distancia

	def getDistancia(self):
		return self.distancia		

	def setCor(self, cor):
		self.cor = cor

	def getCor(self):
		return self.cor

	def setAdjacentes(self, vertice):
		self.adjacentes.append(vertice)
		
	def getAdjacentes(self):
		return self.adjacentes[0].getInfo()

	def setQtdAdjacentes(self, qtd):
		self.qtdAdjacentes = qtd	

	def getQtdAdjacentes(self):
		return self.qtdAdjacentes			

	def setProximo(self, vertice):
		self.proximo = vertice

	def getProximo(self):
		return self.proximo

	def getF(self):
		return self.f

	def setF(self, tempo):
		self.f = tempo

	def getD(self):
		return self.d	

	def setD(self, tempo):
		self.d = tempo	

	def setPredecessor(self, u):
		self.predecessor = u

	def getPredecessor(Self):
		return self.predecessor	

	# Imprime o tempo gasto para achar o nó e tempo que foi necessário para processeça-lo.
	def getTempo(self):
		print("Vertice: %d  %d/%d" %(self.getInfo(), self.getD(), self.getF()))		

	# Imprime a lista de vértices adjacentes.	
	def imprimeListaAdjacentes(self):
		print("Vertices adjacentes ao vertice %d:" %(self.getInfo()))
		for i in range(self.getQtdAdjacentes()):
			print('%d %s' %(self.adjacentes[i].getInfo(), self.adjacentes[i].getCor()))

		print('\n')
	

# Instânciando grafo.
grafo = Grafo()
print('Entre com a quantidade de vertices do grafo:')
grafo.setQtdVertices(int(input()))

# Instânciando vértices.
for i in range(0, grafo.qtdVertices, 1):
	vertice = Vertice()
	vertice.setInfo(i+1)
	grafo.vertices.append(vertice)

# Navegando pelo vetor de vértices do grafo.
for i in range(0,  grafo.qtdVertices, 1):
	
	# Obtendo a quantidade de vértices adjacentes ao vértice da vez.
	print('Digite a quantidade de arestas do vertice: ', grafo.vertices[i].getInfo())
	grafo.vertices[i].setQtdAdjacentes(int(input()))

	# Obtendo os vértices adjacentes do vértice da vez
	for j in range(0, grafo.vertices[i].qtdAdjacentes, 1):
		
		# A info do vértice deve ser passada pois será usada como indice dele no vetor de vértices
		print('Digite as infos dos vertices adjacentes ao vertice: ',grafo.vertices[i].getInfo())
		info = int(input())

		#Adicionando ao vértice da vez um vértice adjacente. Este vértice está no vetor de vértices do grafo na posição  da sua (info -1).
		grafo.vertices[i].setAdjacentes(grafo.vertices[info-1])

print("\n")
#Efetuando busca em profundidade no grafo G.
print("Busca em Profundidade no grafo G:")
grafo.dfs()
grafo.imprimeOrdemTopologica()
print("\n")



# Criango grafo GT transposto a G.
grafoT = Grafo()

# Instânciando vértices.
for i in range(0, grafo.qtdVertices, 1):
	vertice = Vertice()
	vertice.setInfo(i+1)
	vertice.setF(grafo.vertices[i].getF())
	grafoT.vertices.append(vertice)

grafoT.setQtdVertices(grafo.getQtdVertices())

#Navegando por cada vertice do grafo G.
for i in range(grafo.getQtdVertices()):
	# Navegando por cada vertice adjacente ao vértice da vez.
	for j in range(grafo.vertices[i].getQtdAdjacentes()):
		# Armazenando o vértice adjacente.
		vertice = grafo.vertices[i].adjacentes[j]
		# Criando aresta entre o vértice adjacente e o vértice i. de forma a trocas a orientação da aresta.
		grafoT.vertices[vertice.getInfo() -1].adjacentes.append(grafo.vertices[i])
		grafoT.vertices[vertice.getInfo() -1].setQtdAdjacentes(grafoT.vertices[vertice.getInfo() -1].getQtdAdjacentes() +1)	



#Limpando arestas do grafo G.
for i in range(grafoT.getQtdVertices()):
	grafo.vertices[i].adjacentes = []
	grafo.vertices[i].setQtdAdjacentes(0)

print("Calculando a matriz de adjacência transposta ao grafo.\n")
#Atribuindo arestas do grafo GT ao grafo G.
for i in range(grafoT.getQtdVertices()):
	
	for j in range(grafoT.vertices[i].getQtdAdjacentes()):
		grafo.vertices[i].setAdjacentes(grafoT.vertices[i].adjacentes[j])
		grafo.vertices[i].setQtdAdjacentes(grafo.vertices[i].getQtdAdjacentes() + 1)
		

for i in range(grafo.getQtdVertices()):
	print("vertice: %d " %(grafo.vertices[i].getInfo()))		
	grafo.vertices[i].imprimeListaAdjacentes()


print("Efetuando busca em profundidade no grafo Transposto em ordem decrescente de f[u].")
grafo.stronglyConnectedComponents()
grafo.imprimeConjuntosFortementeConexos()
