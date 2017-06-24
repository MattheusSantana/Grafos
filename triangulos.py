#Triângulos.py 
#Esse programa sortea uma cor(branco, cinza, preto) para n vértices de acordo com a probabilidade de cada cor.
#Além disso, para um número sorteado, forma uma aresta entre um par de vértices de acordo com a probabilidade de cada par de cor.
#Por fim é calculado quantos triângulos foram formados, onde cada vértice do triângulo possui cor diferente.
#Programador: Matheus E. Santana
#24/06/2017

import random

class Grafo():
	def __init__(self):
		self.Vertices = [] #Arranjo de vértices do grafo.
		self.branco_preto = 0
		self.branco_cinza = 0
		self.qtdTriangulos = 0

	#Imprime a informação de cada vértice.	
	def imprimeGrafo(self):
		for i in range(len(self.Vertices)):
			print('%d' %(self.Vertices[i].getInfo())) 		

	#Imprime a cor de cada vértice.		
	def imprimeCor(self):
		for i in range(len(self.Vertices)):
			print('%d %s' %(self.Vertices[i].getInfo(), self.Vertices[i].getCor()))			
	
	#Adiciona a probabilidade de arestas entre veŕtices.
	def setProbabilidade(self, branco_preto, branco_cinza):
		self.branco_cinza = branco_cinza
		self.branco_preto = branco_preto

	#Monta o grafo de acordo com a probabilidade e o número sorteado	
	def probabilidade(self, r, vertice_a, vertice_b):
		if(r > 0.0 and r <= self.branco_preto):
			#Caso seja um par (preto, branco)
			if(vertice_a.getCor() == "Branco" and vertice_b.getCor() == "Preto" or vertice_a.getCor() == "Preto" and vertice_b.getCor() == "Branco"):
				print('O vertice %d de cor %s eh adjacente ao vertice %d de cor %s' %(vertice_a.getInfo(), vertice_a.getCor(), vertice_b.getInfo(), vertice_b.getCor()))
				#Adicionando adjacencia entre os pares.
				vertice_a.setAdjacentes(vertice_b)
				vertice_b.setAdjacentes(vertice_a)

			#Caso seja um par (cinza, branco)		
		elif(r > self.branco_preto and r <= self.branco_cinza):
			if(vertice_a.getCor() == "Branco" and vertice_b.getCor() == "Cinza" or vertice_a.getCor() == "Cinza" and vertice_b.getCor() == "Branco"):
				print('O vertice %d de cor %s eh adjacente ao vertice %d de cor %s' %(vertice_a.getInfo(), vertice_a.getCor(), vertice_b.getInfo(), vertice_b.getCor()))
				#Adicionando adjacencia entre os pares.
				vertice_a.setAdjacentes(vertice_b)
				vertice_b.setAdjacentes(vertice_a)
		else:
			#Caso seja um par(preto, cinza)
			if(vertice_a.getCor() == "Preto" and vertice_b.getCor() == "Cinza" or vertice_a.getCor() == "Cinza" and vertice_b.getCor() == "Preto"):
				print('O vertice %d de cor %s eh adjacente ao vertice %d de cor %s' %(vertice_a.getInfo(), vertice_a.getCor(), vertice_b.getInfo(), vertice_b.getCor()))
				#Adicionando adjacencia entre os pares.
				vertice_a.setAdjacentes(vertice_b)
				vertice_b.setAdjacentes(vertice_a)

	#Retorna a quantidade de triângulos formados.			
	def getQtdTriangulos(self):
		return self.qtdTriangulos

	def setQtdTriangulos(self, qtd):
		self.qtdTriangulos = qtd				

	def contaTriangulos(self):
		#Navegando por todos os vértices.
		for i in range(len(self.Vertices)):
			#Navegando em vértices[i+1...n]
			for j in range(i+1, len(self.Vertices)):
			
				#Para um vertice j adj[i,j] faça:
				if(self.Vertices[i].ehAdjacente(self.Vertices[j]) == 1):
					#Se cor(i) != cor(j)
					if(self.Vertices[i].getCor() != self.Vertices[j].getCor()):
						#Navegando em vertices[j+1... n]
						for k in range(j+1, len(self.Vertices)):
						
							#Para um vértice k adj[j, k], faça:
							if(self.Vertices[j].ehAdjacente(self.Vertices[k] )== 1):
								#Se j e k tem cores diferentes.
								if(self.Vertices[j].getCor() != self.Vertices[k].getCor()):
									
									#Para um vértice k onde cor(k) != cor(i), faça:
									if(self.Vertices[k].getCor() != self.Vertices[i].getCor()):
									
										#Se k adj[i,k]
										if(self.Vertices[k].ehAdjacente(self.Vertices[i]) == 1):
										
											#Temos um triangulo formado!
											self.setQtdTriangulos(self.getQtdTriangulos()+1)
											print('%d--%d--%d' %(self.Vertices[i].getInfo(), self.Vertices[j].getInfo(), self.Vertices[k].getInfo()))

		print("%d Triangulos foram formados!"%(self.getQtdTriangulos()))


class Vertice():
	def __init__(self):
		self.info = 0
		self.cor = ""
		self.adjacentes = []
		self.qtdAdjacentes = 0

	def setInfo(self, info):
		self.info = info

	def getInfo(self):
		return self.info	

	def setCor(self, cor):
		self.cor = cor

	def getCor(self):
		return self.cor

	def setAdjacentes(self, vertice):
		self.adjacentes.append(vertice)
		self.setQtdAdjacentes(self.getQtdAdjacentes()+1)
		
	def getAdjacentes(self):
		return self.adjacentes[0].getInfo()

	def setQtdAdjacentes(self, qtd):
		self.qtdAdjacentes = qtd	

	def getQtdAdjacentes(self):
		return self.qtdAdjacentes	

	# Imprime a lista de vértices adjacentes.	
	def imprimeListaAdjacentes(self):
		for i in range(self.getQtdAdjacentes()):
			print('%d %s' %(self.adjacentes[i].getInfo(), self.adjacentes[i].getCor()))

		print('\n')

	#Recebe um vertice v e devolve 1 caso v seja adjacente ao nó que chamou a função. 	
	def ehAdjacente(self, v):
		for i in range(self.getQtdAdjacentes()):
			if(self.adjacentes[i].getInfo() == v.getInfo()):
				return 1
		

grafo = Grafo()
					
print("Informe a quantidade de Vertices!")
qtdVertices = int(input())

#Instânciando e salvando os vértices.
for i in range(qtdVertices):
	vertice = Vertice()
	vertice.info = i
	grafo.Vertices.append(vertice)


print("Informe a probabilidade da cor branca!")
branco = float(input())

print("Informe a probabilidade da cor cinza!")
cinza = float(input())


for i in range(qtdVertices):
	#Sorteando número aleatório.
	r = random.random()
	#Calculando a probabilidade da cor do vértice.
	if(r > 0.0 and r <= branco):
		grafo.Vertices[i].setCor("Branco")
	elif(r > branco and r <= cinza):
		grafo.Vertices[i].setCor("Cinza")
	else:
		grafo.Vertices[i].setCor("Preto")	

print("Informe a probabilidade de uma aresta entre um vertice branco e preto!")
branco_preto = float(input())

print("Informe a probabilidade de uma aresta entre um vertice branco e cinza!")
branco_cinza = float(input())

grafo.setProbabilidade(branco_preto, branco_cinza)

for i in range(qtdVertices):
	print('\n----------Vertice: %d ---------- ' %(grafo.Vertices[i].getInfo()))
	for j in range(i+1, qtdVertices):
		#Sorteando número aleatório.
		r = random.random()
		#Calculando a probabilidade da formação de arestas entre todos os vértices do grafo.
		grafo.probabilidade(r, grafo.Vertices[i], grafo.Vertices[j])

#Imprimindo a quantidade de arestas.
grafo.contaTriangulos()