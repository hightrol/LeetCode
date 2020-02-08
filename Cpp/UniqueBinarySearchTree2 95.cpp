/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> buildTrees(vector<int> &vec){
        TreeNode *p;
        vector<TreeNode*> res;
        if(vec.empty()){
            p = NULL;
            res.push_back(p);
        } else {
            int n = vec.size();
            for(int i = 0; i < n; i++){
                vector<int> vec1 = vector<int>(vec.begin(), vec.begin()+i);
                vector<int> vec2 = vector<int>(vec.begin()+(i+1), vec.end()); 
                vector<TreeNode*> res1 = buildTrees(vec1);
                vector<TreeNode*> res2 = buildTrees(vec2);
                for(auto p1: res1){
                    for(auto p2: res2){
                        p = new TreeNode(vec[i]);
                        p->left = p1;
                        p->right = p2;
                        res.push_back(p);
                    }
                }
            }
        }
        return res;
    }
    
    vector<TreeNode*> generateTrees(int n) {
        if(n==0){
            vector<TreeNode*> res;
            return res;
        }
        vector<int> vec = {};
        for(int i=1; i<=n; i++){
            vec.push_back(i);
        }
        return buildTrees(vec);
    }
};
