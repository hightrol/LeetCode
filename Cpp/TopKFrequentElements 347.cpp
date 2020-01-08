class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> counter;
        priority_queue <vector<int>> pq;
        vector<int> ans;
        for (int i: nums){
            if (counter.count(i)){
                counter[i] += 1;
            } else {
                counter[i] = 1;
            }
        } 
        for (auto pair: counter){
            vector<int> temp = {-pair.second, pair.first};
            pq.push(temp);
            if(pq.size() > k){
                pq.pop();
            }
        }
        while(pq.size()>0){
            ans.push_back(pq.top()[1]);
            pq.pop();
        }
        return ans;
    }
};
