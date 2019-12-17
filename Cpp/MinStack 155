class MinStack {
public:
    /** initialize your data structure here. */
    int curMin = INT_MAX;
    stack <int> s;
    
    void push(int x) {
        if (x <= curMin){
            s.push(curMin);
            curMin = x;
        } 
        s.push(x);
    }
    
    void pop() {
        int top = s.top();
        s.pop();
        if (top == curMin){
            curMin = s.top();
            s.pop();
        }
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return curMin;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
