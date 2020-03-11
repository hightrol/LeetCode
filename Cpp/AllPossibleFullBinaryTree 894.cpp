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
    vector<TreeNode*> all_possible_FBT(int N){
        vector<TreeNode*> res;
        if(N == 1){
            TreeNode *p1 = new TreeNode(0);
            res.push_back(p1);
        } else if(N%2 == 1){
            for(int i=1; i<N; i+=2){
                vector<TreeNode*> lefts = allPossibleFBT(i);
                vector<TreeNode*> rights = allPossibleFBT(N-i-1);
                for(auto &ltree: lefts){
                    for(auto &rtree: rights){
                        TreeNode *p1 = new TreeNode(0);
                        p1->left = ltree;
                        p1->right = rtree;
                        res.push_back(p1);
                    }
                }
            }
        }
        return res;
    }
    
    vector<TreeNode*> allPossibleFBT(int N) {
        map <int, vector<TreeNode*>> resMap;
        if(resMap.count(N) == 0){
            resMap[N] = all_possible_FBT(N);
        }
        return resMap[N];
    }
};
