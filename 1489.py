class UnionFind:
    def __init__(self, n):
        # Cada nó começa como seu próprio pai (representante do conjunto)
        self.pai = list(range(n))
        # 'rank' para balancear as árvores na hora de unir os conjuntos
        self.rank = [0] * n

    def encontrar(self, x):
        # Encontra o representante (raiz) do conjunto de x com compressão de caminho
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])
        return self.pai[x]

    def unir(self, x, y):
        # Une os conjuntos de x e y. Retorna True se conseguiu unir, False se já estavam juntos
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        if raiz_x == raiz_y:
            return False
        # Une o conjunto de menor rank ao de maior rank
        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        else:
            self.pai[raiz_y] = raiz_x
            if self.rank[raiz_x] == self.rank[raiz_y]:
                self.rank[raiz_x] += 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        # Adiciona o índice original de cada aresta para rastrear depois
        for i in range(len(edges)):
            edges[i].append(i)

        # Ordena as arestas por peso (como no algoritmo de Kruskal)
        edges.sort(key=lambda x: x[2])

        # Função que calcula o custo da MST com opção de ignorar ou forçar uma aresta
        def kruskal(ignorar=None, forcar=None):
            uf = UnionFind(n)
            custo_total = 0

            if forcar is not None:
                a, b, peso, _ = edges[forcar]
                if uf.unir(a, b):
                    custo_total += peso

            # percorre todas as arestas
            for i in range(len(edges)):
                if i == ignorar:
                    continue
                a, b, peso, _ = edges[i]
                if uf.unir(a, b):
                    custo_total += peso

            # Verifica se conecta todos os nós
            conjuntos = set()
            for i in range(n):
                conjuntos.add(uf.encontrar(i))
            if len(conjuntos) > 1:
                return float('inf')  # Não é uma MST válida

            return custo_total

        # custo da MST original
        custo_mst_original = kruskal()

        arestas_criticas = []         # Arestas que, se removidas, aumentam o custo da MST
        arestas_pseudo_criticas = []  # Arestas que podem estar na MST, mas não são essenciais

        # testa cada aresta
        for i in range(len(edges)):
            # Se ao ignorar a aresta o custo da MST aumenta, ela é crítica
            if kruskal(ignorar=i) > custo_mst_original:
                arestas_criticas.append(edges[i][3])
            # Se ao forçar a aresta o custo continua o mesmo, ela é pseudo-crítica
            elif kruskal(forcar=i) == custo_mst_original:
                arestas_pseudo_criticas.append(edges[i][3])

        return [arestas_criticas, arestas_pseudo_criticas]
