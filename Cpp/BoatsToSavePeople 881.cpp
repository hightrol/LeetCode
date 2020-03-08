class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int n = people.size();
        int i = 0, j = n-1;
        int total = 0;
        while(i <= j){
            if(people[i] + people[j] <= limit){
                total += 1;
                i += 1;
                j -= 1;
            } else {
                j -= 1;
                total += 1;
            }
        }
        return total;
    }
};
