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
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> nodes;
        stack<int> vals;
        vector<int> res;
        if(root){
            nodes.push(root);            
        }
        while(!nodes.empty()){
            TreeNode* node = nodes.top();
            nodes.pop();
            vals.push(node->val);
            if(node->left){
                nodes.push(node->left);
            }
            if(node->right){
                nodes.push(node->right);
            }            
        }
        while(!vals.empty()){
            res.push_back( vals.top() );
            vals.pop();
        }
        return res;
    }
};
