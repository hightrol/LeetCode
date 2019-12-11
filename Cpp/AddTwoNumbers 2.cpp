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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int a = 0, b = 0;
        int digitSum;
        ListNode *p = new ListNode(0);
        ListNode *dummy = p;
        while(l1 or l2 or a){
            p->next = new ListNode(0);
            int l1Add = (!l1) ? 0 : l1->val;
            int l2Add = (!l2) ? 0 : l2->val;
            digitSum = l1Add + l2Add + a;
            a = digitSum / 10;
            b = digitSum % 10;
            if (l1){
                l1 = l1->next;
            }
            if (l2){
                l2 = l2->next;
            }
            p = p->next;
            p->val = b;
        }        
        return dummy->next;
    }
};
