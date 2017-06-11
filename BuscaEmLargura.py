#Busca Em Largura BFS
#Programador: Matheus Santana.
# 10/06/2017

class Grafo():
	def __init__(self):
		self.qtdVertices = 0	 	# Armazena a quantidade de vértices do grafo.	
		self.qtdMaxAdjacentes = 0	# Armazena a quantiadde máxima de arestas para cada grafo.
		self.vertices = []			# Armazena os vértices.
		self.verticesEmNivel = []	# Armazena os vértices em ordem de nível após a BFS.


	def setQtdVertices(self, qtd):
		self.qtdVertices = qtd	

	def getQtdVertices(self):
		return self.qtdVertices

	def setVerticesEmNivel(self, no):
		self.verticesEmNivel.append(no)	


	#Recebe um grafo, uma fila e uma posição referente ao vértice inicial.	
	def buscaEmLargura(self, posicao, fila):
			# 1 - Marcando o grafo de cinza.
			self.vertices[posicao].setCor('Cinza')

			# 2 - Iniciando a fila.
			fila.enfileira(self.vertices[posicao])

			# Enquanto tiver elementos na fila.
			while(fila.getVazia() != True):
				i = 0
				# - Desenfileirando vértice.
				v = fila.desenfileira()

				# - Processando o vértice.
				self.setVerticesEmNivel(v)

				i += 1
				# Marcando os vértices adjacentes, brancos, de v como cinza.
				for j in range(0, v.qtdAdjacentes, 1):
					if(v.adjacentes[j].getCor() == 'Branco'):
						v.adjacentes[j].setCor('Cinza')
						
						# Incrementando a distância do vértice adj[v].
						v.adjacentes[j].setDistancia = v.getDistancia() + 1
						fila.enfileira(v.adjacentes[j])
				#Finaliza o grafo.		
				v.setCor('Preto')

	# Retorna o vetor de vértices em Nível.
	def getVerticesEmNivel(self):
		for k in range(self.getQtdVertices()):
			print('Vertice: %d' %(self.verticesEmNivel[k].getInfo()))			


class Vertice():
	def __init__(self):
		self.info = None		# Armazena o valor do vertice.
		self.distancia = 0		# Distância até um determinado vértice.
		self.cor = 'Branco'		# Iniciando vértice como não marcado.
		self.adjacentes = []	# Recebe vértices adjacentes.
		self.qtdAdjacentes = 0	# Quantidade de arestas do vértice
		self.proximo = None		# Ponteiro para o próximo vértice na fila.

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
			

	# Imprime a lista de vértices adjacentes.	
	def imprimeListaAdjacentes(self):
		for i in range(self.getQtdAdjacentes()):
			print('%d %s' %(self.adjacentes[i].getInfo(), self.adjacentes[i].getCor()))

		print('\n')

class Fila():
	def __init__(self):
		self.inicio = None
		self.fim = None 
		self.vazia = True

	def setInicio(self, no):
		self.inicio = no

	def getInicio(self):
		return self.inicio

	def setFim(self, no):
		self.fim = no

	def getFim(self):
		return self.fim	

	def getVazia(self):
		return self.vazia

	def setVazia(self, booleano):
		self.vazia = booleano
		
	def enfileira(self, no):
		# Se a fila está vazia
		if(self.getVazia() == True):
			self.setInicio(no)
			self.setFim(no)
			self.setVazia(False)
		# Se a fila tem pelo menos um elemento.
		else:
			self.getFim().setProximo(no)
			self.setFim(no)	

	def desenfileira(self):
		# Se a fila estiver vazia.
		if(self.getVazia() == True):
			return print('A pilha está vazia!')
		# Se a fila contém pelo menos um elemento.	
		else:
			#Se a fila contém apenas um elemento.
			if(self.getInicio().getProximo() == None):
				no = self.getInicio()
				self.setInicio(None)
				self.setFim(None)
				self.setVazia(True)
			# Se a fila contém mais de um elemento.
			else:
				no = self.getInicio()
				self.setInicio(self.getInicio().getProximo())
		return no		

	# Imprime estado atual da fila.	
	def imprimeFila(self):
		i = self.getInicio()
		while(i != None):
			print('%d' %(i.getInfo()))	
			i = i.getProximo()

# Instânciando grafo.
grafo = Grafo()
print('Entre com a quantidade de vertices do grafo:')
grafo.setQtdVertices(int(input()))
print('Entre com a quantidade maxima de arestas para todos os vértices')
grafo.qtdMaxAdjacentes = int(input())

# Instânciando vértices.
for i in range(0, grafo.qtdVertices, 1):
	print('Digite a informacao do vertice: ', i+1)
	vertice = Vertice()
	vertice.setInfo(int(input()))
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

fila = Fila()
grafo.buscaEmLargura(0, fila)
grafo.getVerticesEmNivel()