class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        int INF = 1000000;
        vector<vector<int>> graph(N, vector<int>(N, INF));
        vector<int> dist(N,0);
        set<int> S;
        int last;
        for(auto edge: times){
            graph[edge[0]-1][edge[1]-1] = edge[2];
        }
        for(int j=0; j<N; j++){
            S.insert(j);
            graph[j][j] = 0;
            dist[j] = graph[K-1][j];
        }
        while(!S.empty()){
            int ix;
            int res = INF;
            for(int j: S){
                if(dist[j] < res){
                    res = min(dist[j], res);
                    ix = j;
                }
            }
            if(res == INF){
                return -1;
            }
            S.erase(ix);
            for(int j: S){
                dist[j] = min(dist[ix] + graph[ix][j], dist[j]);
                last = dist[j];
            }
        }
        return last;
        
    }
};
