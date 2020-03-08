/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *head;
    ListNode *cur;
    ListNode *select;
    int pass;
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        this->head = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int randNum;
        int pass = 1;
        cur = select = head;
        while(cur != NULL){
            randNum = rand()%pass;
            if(randNum == 1){
                select = cur;
            }
            pass += 1;
            cur = cur->next;
        }
        return select -> val;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
