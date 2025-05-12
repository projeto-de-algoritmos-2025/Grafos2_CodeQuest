
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        const int INF = numeric_limits<int>::max();

        vector<vector<pair<int, int>>> adj(n + 1);
        for (const auto& time : times) {
            int u = time[0]; // Nó de origem
            int v = time[1]; // Nó de destino
            int w = time[2]; // Tempo (peso)
            adj[u].push_back({v, w});
        }

        // Inicializar vetor de distâncias
        // dist[i] = menor tempo conhecido para chegar ao nó i a partir de k
        vector<int> dist(n + 1, INF);

        // Armazena pares {distancia_atual, no}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        // Começar o algoritmo de Dijkstra a partir do nó k
        dist[k] = 0;
        pq.push({0, k}); 

        while (!pq.empty()) {
            int d = pq.top().first;  // Distância atual para o nó u
            int u = pq.top().second; // Nó atual
            pq.pop();

        
            if (d > dist[u]) {
                continue;
            }

            // Relaxar arestas saindo de u
            for (const auto& edge : adj[u]) {
                int v = edge.first;       // Vizinho
                int weight = edge.second; // Peso da aresta u -> v

                if (dist[u] != INF && dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight; // Atualiza a distância
                    pq.push({dist[v], v});      // Adiciona/atualiza na fila de prioridade
                }
            }
        }

        // Calcular o resultado final
        int max_delay = 0;
        for (int i = 1; i <= n; ++i) {
            // Se algum nó for inalcançável (distância ainda é INF)
            if (dist[i] == INF) {
                return -1;
            }
            // Encontra o tempo máximo para alcançar qualquer nó
            max_delay = max(max_delay, dist[i]);
        }

        return max_delay;
    }
};