class Solution {
public:

    int pivotIx(vector<int>& dict, int s, int e, int pivot){
        /* 
        return the first index larger than pivot
        smaller on the left and larger on the right
        */
        int i = s, j = e-1;
        while (i <= j){
            if (dict[i] < pivot){
                i += 1;
            } else {
                int temp = dict[i];
                dict[i] = dict[j];
                dict[j] = temp;
                j -= 1;
            }
        }
        return i;
    }
    
    int findKthSmallest(vector<int>& dict, int s, int e, int k){
        if (e-s == 1){
            return dict[s];
        } else if (e-s == 2){
            return (k==1) ? min(dict[s], dict[e-1]): max(dict[s], dict[e-1]);
        } else {
            int mid = (s+2*(e-1))/3;
            int ix = pivotIx(dict, s, e, dict[mid]);
            if (ix < s+k){
                return findKthSmallest(dict, ix, e, k-(ix-s));
            } else {
                return findKthSmallest(dict, s, ix, k);
            }            
        }        
    }
    
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        vector<int> dist;
        int n = points.size();
        if (K == n){
            return points;
        }
        vector<vector<int>> res;
        for (int i=0; i<n; i++){
            vector<int> point = points[i];
            dist.push_back( point[0]*point[0] + point[1]*point[1] );
        }
        int pivot = findKthSmallest(dist, 0, n, K);
        for (int i=0; i<n; i++){
            if (points[i][0]*points[i][0] + points[i][1]*points[i][1] <= pivot){
                res.push_back( points[i] );
            }
        }
        return res;
    }
    
};
