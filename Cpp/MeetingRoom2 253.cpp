/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
     
    bool static compareInterval(Interval &a,  Interval &b){
        if( a.start < b.start ){
            return true;
        } else if ( a.start > b.start ){
            return false;
        } else if ( a.end > b.end ){
            return false;
        } else {
            return true;
        }
    }
     
    int minMeetingRooms(vector<Interval> &intervals) {
        // Write your code here
        priority_queue<int> pq;
        sort(intervals.begin(), intervals.end(), compareInterval);
        int res = 0;
        int size = 0;
        for (auto ea: intervals){
            while(!pq.empty() and ea.start > -pq.top()){
                pq.pop();
                size -= 1;
            } 
            pq.push(-ea.end);
            size += 1;
            res = max( res, size );
        }
        return res;
    }
    
};
