#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define print_vec(v) { rep(i, v.size()) cout << v[i] << " "; cout << endl; }
#define ll long long
const int MOD = 998244353;
const int INF = 1000000000;
const ll INFll = 9223372036854775807;

struct maxflow_edge{
    int to, cap, rev_idx;
};

class maximumflow{
    public:
        vector<vector<maxflow_edge>> G;
        vector<bool> vis;

        void init(int N){
            G.resize(N+1);
            vis.resize(N+1,false);
        }

        void add_edge(int a, int b, int c){
            int ga_size = G[a].size();
            int gb_size = G[b].size();
            G[a].emplace_back(maxflow_edge{b,c,gb_size});
            G[b].emplace_back(maxflow_edge{a,0,ga_size});
        }

        int dfs(int v, int goal, int f){
            if (v==goal) return f;
            vis[v] = true;
            for (auto &edge : G[v]){
                if (edge.cap == 0) continue;
                if (vis[edge.to]) continue;
                int flow = dfs(edge.to, goal, min(f, edge.cap));
                if (flow > 0){
                    edge.cap -= flow;
                    G[edge.to][edge.rev_idx].cap += flow;
                    return flow;
                }
            }
            return 0;
        }

        int maxflow(int N, int M, int start, int goal){
            int total_flow = 0;
            while (true){
                for (int i=0; i<=N; i++) vis[i] = false;
                const int INF = 1000000000;
                int res = dfs(start,goal,INF);
                if (res==0) break;
                total_flow += res;
            }
            return total_flow;
        }
};
