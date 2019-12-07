class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int l = 0, r = n-1;
        int res;
        if ( n == 0 ){
            return -1;
        }
        if ( n == 1){
            return (nums[0] == target) ? 0 : -1; 
        }
        // nums[:l] and nums[l:] are two increasing arr
        while (l < r){
            int mid = (l+r)/2 ;
            if (nums[mid] > nums[n-1]){
                l = mid+1;
            } else {
                r = mid;
            }
        }
        cout << 'turning point:' << l;
        
        if(target > nums[n-1]){
            res = binarySearch(nums, 0, l, target);
        } else {
            res = binarySearch(nums, l, n, target);
        }
        return res;
    }
    
    // binarySearch find target or return -1
    int binarySearch(vector<int>& arr, int l, int r, int target){
        int n = arr.size();
        if ((0 <= l) and (r <= n)){
            while (l < r){
                int mid = (l+r)/2 ;
                if (arr[mid] < target){
                    l = mid+1;
                } else {
                    r = mid;
                }
            }  
            return (arr[l] == target) ? l : -1;           
        }
        return -1;
    }
    
    
};
