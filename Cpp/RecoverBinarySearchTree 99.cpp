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
    vector<TreeNode*> vec;
    
    void preorder(TreeNode* root){
        if(root){
            preorder(root->left);
            vec.push_back(root);
            preorder(root->right);
        }        
    }
    
    void recoverTree(TreeNode* root) {
        preorder(root);
        int n = vec.size();
        int i, j, k = 0;
        for(k = 0; k < n-1; k++){
            if(vec[k]->val > vec[k+1]->val){
                i = k;
                break;
            }
        }
        for(k = n-1; k > 0; k--){
            if(vec[k]->val < vec[k-1]->val){
                j = k;
                break;
            }
        }
        int temp = vec[i]->val;
        vec[i]->val = vec[j]->val;
        vec[j]->val = temp;
    }
};
