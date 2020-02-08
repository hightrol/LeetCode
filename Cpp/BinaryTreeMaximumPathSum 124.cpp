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
    map <TreeNode*, int> maxSumOneSide;
    int maxSum = -100000;
    
    int helper(TreeNode* root){
        if(root){
            int res1 = helper(root->left);
            int res2 = helper(root->right);
            int maxSumWithRoot = root->val + max(res1, 0) + max(res2, 0);
            if (maxSumWithRoot > maxSum){
                maxSum = maxSumWithRoot;
            }
            int res = root->val + max({res1, res2, 0});
            maxSumOneSide[root] = res;
            return res;
        }
        return 0;
    }
    
    int maxPathSum(TreeNode* root) {
        helper(root);
        return maxSum;
    }
};
