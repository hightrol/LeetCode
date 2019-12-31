class Solution {
public:
    bool dfs(int i, vector<vector<int>> &required, vector<int> &visit){
        visit[i] = 0;
        for (auto j: required[i]){
            if(visit[j] == -1){
                bool success = dfs(j, required, visit);
                if(!success){
                    return false;
                }
            }
            else if(visit[j] == 0){
                return false;
            }
        }
        visit[i] = 1;
        return true;
    }
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> required(numCourses, vector<int>());
        vector<int> visit(numCourses, -1);
        for (vector<int> req: prerequisites){
            required[req[0]].push_back(req[1]);
        }
        for (int i = 0; i < numCourses; i++){
            if (visit[i] == -1){
                bool success = dfs(i, required, visit);
                if(!success){
                    return false;
                }
            }
            else if (visit[i] == 0){
                return false;
            }
        }
        for (int i = 0; i < numCourses; i++){
            if (visit[i] != 1){
                return false;
            }
        }
        return true;
    }
};
