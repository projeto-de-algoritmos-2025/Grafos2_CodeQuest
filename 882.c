const int INF = std::numeric_limits<int>::max();

class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
        // 1. Construir lista de adjacência para Dijkstra
        // adj[u] armazena pares {vizinho_v, peso_para_v}
        std::vector<std::vector<std::pair<int, int>>> adj(n);
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int cnt = edge[2]; // número de novos nós nesta aresta
            adj[u].push_back({v, cnt + 1});
            adj[v].push_back({u, cnt + 1});
        }

        // 2. Algoritmo de Dijkstra a partir do nó 0
        std::vector<int> dist(n, INF);
        std::priority_queue<std::pair<int, int>, 
                            std::vector<std::pair<int, int>>, 
                            std::greater<std::pair<int, int>>> pq;

        dist[0] = 0;
        pq.push({0, 0});

        while (!pq.empty()) {
            auto [current_moves, u] = pq.top();
            pq.pop();

            // Se já encontramos um caminho mais curto para u, ou esta é uma entrada obsoleta
            if (current_moves > dist[u]) {
                continue;
            }

            for (auto& edge_info : adj[u]) {
                int v = edge_info.first;
                int weight = edge_info.second; // custo para atravessar de u para v (cnt + 1)
                
                // Se current_moves + weight for menor que a distância conhecida para v
                if (current_moves + weight < dist[v]) {
                    dist[v] = current_moves + weight;
                    pq.push({dist[v], v});
                }
            }
        }

        // 3. Contar nós originais alcançáveis
        int total_reachable_nodes = 0;
        for (int i = 0; i < n; ++i) {
            if (dist[i] <= maxMoves) { // Se o nó original i é alcançável dentro de maxMoves
                total_reachable_nodes++;
            }
        }

        // 4. Contar nós de subdivisão alcançáveis
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int cnt_subdivision_nodes_on_edge = edge[2]; 

            // Calcular quantos movimentos restam para explorar de u em direção a v
            long long moves_left_from_u = 0;
            if (dist[u] <= maxMoves) { 
                moves_left_from_u = maxMoves - dist[u];
            }

            // Calcular quantos movimentos restam para explorar de v em direção a u
            long long moves_left_from_v = 0;
            if (dist[v] <= maxMoves) { 
                moves_left_from_v = maxMoves - dist[v];
            }
        
            total_reachable_nodes += std::min((long long)cnt_subdivision_nodes_on_edge, 
                                              moves_left_from_u + moves_left_from_v);
        }
        
        return total_reachable_nodes;
    }
};