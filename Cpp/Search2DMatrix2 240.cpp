class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if (m == 0){
            return false;
        }
        int n = matrix[0].size();
        int i = 0, j = n-1;
        while ( i < m and j >= 0 ){
            if ( matrix[i][j] < target ){
                i += 1;
            } else if (matrix[i][j] > target) {
                j -= 1;
            } else {
                return true;
            }
        }
        return false;
    }
};
