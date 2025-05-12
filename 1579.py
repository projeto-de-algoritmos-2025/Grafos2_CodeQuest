class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))  # Cada nó começa como seu próprio pai
        self.rank = [0] * n        # Usado para otimizar as uniões
        self.componentes = n       # Inicialmente temos n componentes separados

    # Função para encontrar o representante (raiz) do conjunto do elemento x
    def encontrar(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])  # Otimização: path compression
        return self.pai[x]

    # Função para unir dois conjuntos
    def unir(self, x, y):
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)
        if raiz_x == raiz_y:
            return False  # Já estão no mesmo conjunto, união desnecessária
        # União por rank (altura da árvore)
        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        else:
            self.pai[raiz_y] = raiz_x
            if self.rank[raiz_x] == self.rank[raiz_y]:
                self.rank[raiz_x] += 1
        self.componentes -= 1  # Menos uma componente isolada
        return True

class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        removidas = 0

        # Etapa 1: processa as arestas do tipo 3 (usadas por ambos)
        for tipo, u, v in edges:
            if tipo == 3:
                uniao_alice = uf_alice.unir(u - 1, v - 1)
                uniao_bob = uf_bob.unir(u - 1, v - 1)
                if not uniao_alice and not uniao_bob:
                    removidas += 1  # Aresta não necessária para nenhum dos dois

        # Etapa 2: processa arestas do tipo 1 (apenas Alice)
        for tipo, u, v in edges:
            if tipo == 1:
                if not uf_alice.unir(u - 1, v - 1):
                    removidas += 1  # Já conectados, aresta redundante

        # Etapa 3: processa arestas do tipo 2 (apenas Bob)
        for tipo, u, v in edges:
            if tipo == 2:
                if not uf_bob.unir(u - 1, v - 1):
                    removidas += 1  # Redundante

        # Verifica se ambos estão conectados (1 única componente)
        if uf_alice.componentes > 1 or uf_bob.componentes > 1:
            return -1  # Não é possível manter a conectividade para ambos

        return removidas  # Número máximo de arestas que podem ser removidas
