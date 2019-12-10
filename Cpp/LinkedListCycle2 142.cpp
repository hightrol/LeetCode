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
    ListNode *detectCycle(ListNode *head) {
        if (!head){
            return NULL;
        }
        ListNode *fast = head, *slow = head;
        int pos = -1;
        while (fast->next and fast->next->next){
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow){
                fast = head;
                pos = 0;
                while(fast != slow){
                    fast = fast->next;
                    slow = slow->next;
                    pos += 1;
                }
                return fast;
            }
        }
        return NULL;
    }
};
