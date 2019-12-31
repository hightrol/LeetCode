class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        int n = A.size();
        vector<int> cumsum = {0};
        deque<int> q;
        int res = n+1;
        for(int i = 1; i < n+1; i++){
            cumsum.push_back(cumsum[i-1] + A[i-1]);
        }
        for(int i = 0; i < n+1; i++){
            while(!q.empty() and cumsum[q.front()] <= cumsum[i]-K){
                res = min(res, i-q.front());
                q.pop_front();
            }
            while(!q.empty() and cumsum[q.back()] >= cumsum[i]){
                    q.pop_back();
            }
            q.push_back(i);
        }
        return (res > n)?-1:res;
    }
};
