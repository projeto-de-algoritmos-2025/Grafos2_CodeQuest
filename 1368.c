class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;

        vector<vector<int>> dist(m, vector<int>(n, numeric_limits<int>::max()));

        using State = pair<int, pair<int, int>>; // {custo, {linha, coluna}}
        priority_queue<State, vector<State>, greater<State>> pq;

        // Sistema de navegação na matriz
        int dr[] = {0, 0, 1, -1};
        int dc[] = {1, -1, 0, 0};

        // Começa em (0, 0) com custo 0
        dist[0][0] = 0;
        pq.push({0, {0, 0}}); // Adiciona o ponto inicial à fila

        while (!pq.empty()) {
            auto top = pq.top();
            pq.pop();

            int current_cost = top.first;
            int r = top.second.first;
            int c = top.second.second;

            if (current_cost > dist[r][c]) {
                continue;
            }

            // Se chegamos ao destino, encontramos o caminho de menor custo
            if (r == m - 1 && c == n - 1) {
                return current_cost;
            }

            // Obtém a direção preferida da célula atual (ajustando para índice 0)
            int preferred_direction_index = grid[r][c] - 1;

            // Explora todos os 4 movimentos possíveis a partir de (r, c)
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k]; 
                int nc = c + dc[k]; 

                // Verifica se a nova célula está dentro dos limites da grade
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int move_cost = (k == preferred_direction_index) ? 0 : 1;
                    int new_cost = current_cost + move_cost;

                    // Se encontrarmos um caminho mais barato para (nr, nc)
                    if (new_cost < dist[nr][nc]) {
                        dist[nr][nc] = new_cost; 
                        pq.push({new_cost, {nr, nc}});
                    }
                }
            }
        }
        return dist[m - 1][n - 1];
    }
};