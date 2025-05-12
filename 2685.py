from collections import defaultdict

# Classe que representa a estrutura Union-Find
class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))  # Cada nó começa sendo seu próprio pai
    
    def encontrar(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])  # Compressão de caminho
        return self.pai[x]
    
    def unir(self, x, y):
        self.pai[self.encontrar(x)] = self.encontrar(y)  # Une os conjuntos

class Solution:
    def countCompleteComponents(self, n, arestas):
        uf = UnionFind(n)

        # Une os nós conectados por arestas
        for a, b in arestas:
            uf.unir(a, b)

        componentes = defaultdict(set)  # Dicionário para guardar os nós de cada componente
        qtd_arestas = defaultdict(int)  # Conta quantas arestas existem em cada componente

        # Agrupa os nós em seus respectivos componentes
        for i in range(n):
            raiz = uf.encontrar(i)
            componentes[raiz].add(i)

        # Conta as arestas por componente
        for a, b in arestas:
            raiz = uf.encontrar(a)
            qtd_arestas[raiz] += 1

        # Conta quantas componentes são completas
        completas = 0
        for raiz in componentes:
            tamanho = len(componentes[raiz])  # Número de nós no componente
            arestas_esperadas = tamanho * (tamanho - 1) // 2
            if qtd_arestas[raiz] == arestas_esperadas:
                completas += 1

        return completas
