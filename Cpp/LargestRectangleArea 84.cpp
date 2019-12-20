class Solution {
public:
    int largestRectangleArea(vector<int> heights) {
        heights.insert(heights.begin(), 0);
        heights.push_back(0);
        stack <int> s;
        int n = heights.size();
        int res = 0;
        for (int i = 0; i < n; i = i+1){
            int hi = heights[i];
            while(!s.empty() and hi < heights[s.top()]){
                int j = s.top();
                s.pop();
                int width = s.empty() ? (i - j) : (i - s.top() - 1);
                res = max(res, heights[j] * width);
            }
            s.push(i);
        }
        return res;
    }
};
