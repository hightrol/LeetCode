class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> mymap1;
        map<int, int> mymap2;
        vector<int> res;
        for (int i: nums1){
            mymap1[i] = mymap1[i] + 1;
        }
        for (int i: nums2){
            mymap2[i] = mymap2[i] + 1;
        }
        for (auto pair: mymap1){
            int x = min(mymap1[pair.first], mymap2[pair.first]);
            for (int k=0; k<x; k++){
                res.push_back(pair.first);
            }
        }
        return res;
    }
};
