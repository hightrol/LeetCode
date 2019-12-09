class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size();
        if ( (n1+n2)%2 == 0 ){
            int k = (n1+n2)/2;
            double res1 = findKthSortedArrays(nums1, nums2, 0, n1, 0, n2, k);
            double res2 = findKthSortedArrays(nums1, nums2, 0, n1, 0, n2, k+1);
            return ( res1 + res2 )/2;
        } else {
            int k = (n1+n2+1)/2;
            double res = findKthSortedArrays(nums1, nums2, 0, n1, 0, n2, k);
            return res;
        }
    }
    
    
    int binarySearchIndex(vector<int> nums, int s, int e, int target){
        int l = s, r = e;
        if (nums[s]>= target){
            return s;
        } else if (nums[e-1] <= target){
            return e;
        }
        while (l < r){
            int mid = (l+r)/2;
            if (nums[mid] < target){
                l = mid+1;
            } else{
                r = mid;
            }
        }
        return l;
    }
    
    double findKthSortedArrays(vector<int>& nums1, vector<int>& nums2, int s1, int e1, int s2, int e2, int k){
        if ( e1 == s1 ){
            return nums2[k+s2-1];
        } else if ( e2 == s2 ){
            return nums1[k+s1-1];
        } else if ( e1-s1 == 1 ){
            int ix = binarySearchIndex(nums2, s2, e2, nums1[s1]);
            if (k+s2>ix+1) {
                return nums2[s2+k-2];
            } else if (k+s2<ix+1){
                return nums2[s2+k-1];
            } else {
                return nums1[s1];
            }
        } else if ( e2-s2 == 1){
            int ix = binarySearchIndex(nums1, s1, e1, nums2[s2]);
            if (k+s1>ix+1) {
                return nums1[s1+k-2];
            } else if (k+s1<ix+1){
                return nums1[s1+k-1];
            } else {
                return nums2[s2];
            }
        }
        else {
            int m1 = (s1+e1)/2;
            int m2 = (s2+e2)/2;
            if (k > (m1-s1 + m2-s2)){
                if (nums1[m1] <= nums2[m2]){
                    return findKthSortedArrays(nums1, nums2, m1, e1, s2, e2, k-(m1-s1));
                } else {
                    return findKthSortedArrays(nums1, nums2, s1, e1, m2, e2, k-(m2-s2));
                }                
            } else {
                if (nums1[m1] <= nums2[m2]){
                    return findKthSortedArrays(nums1, nums2, s1, e1, s2, m2, k);
                } else {
                    return findKthSortedArrays(nums1, nums2, s1, m1, s2, e2, k);
                }                   
            }
        }
    }
    
};
