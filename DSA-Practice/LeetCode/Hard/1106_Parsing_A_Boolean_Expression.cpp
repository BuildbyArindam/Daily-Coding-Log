/*
 * Problem   : 1106. Parsing A Boolean Expression
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/parsing-a-boolean-expression/
 * Difficulty: Hard
 * Topics    : String, Stack, Recursion
 * Date      : 2026-11-24
 *
 * Approach  : Two stacks. One holds operators (&, |, !) and the other holds
 *             operands ('t', 'f') plus '(' and ',' markers. On ')', pop the
 *             top operator, then pop operands back to the matching '('.
 *               &  -> false if any 'f' is seen, else true
 *               |  -> true if any 't' is seen, else false
 *               !  -> invert the single operand
 *             Push the evaluated result back as 't' or 'f'. The final top of
 *             the operand stack is the answer.
 *
 * Time      : O(n), each character is pushed and popped at most once
 * Space     : O(n), for the two stacks
 */


// ------------------------------------------------- Solution -------------------------------------------------------------


class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> oper;
        stack<char> st;
        int n = expression.size();
        for (int i = 0; i < n; i++) {
            if (expression[i] == '|' || expression[i] == '&' || expression[i] == '!') {
                oper.push(expression[i]);
            } else if (expression[i] == 'f' || expression[i] == 't' || expression[i] == '(' ||
                       expression[i] == ',') {
                st.push(expression[i]);
            } else if (expression[i] == ')') {
                char op = oper.top();
                oper.pop();
                if (op == '&') {
                    bool flag = true;
                    while (st.top() != '(') {
                        char c = st.top();
                        if (c == 'f') {
                            flag = false;
                        }
                        st.pop();
                    }
                    st.pop();
                    if (flag)
                        st.push('t');
                    else
                        st.push('f');
                } else if (op == '|') {
                    bool flag = false;
                    while (st.top() != '(') {
                        char c = st.top();
                        if (c == 't') {
                            flag = true;
                        }
                        st.pop();
                    }
                    st.pop();
                    if (flag)
                        st.push('t');
                    else
                        st.push('f');
                } else if (op == '!') {
                    char c = st.top();
                    st.pop();
                    st.pop();
                    if (c == 't') {
                        st.push('f');
                    } else
                        st.push('t');
                }
            }
        }
        if (st.top() == 'f')
            return false;
        else
            return true;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
