class Solution {
public:
    string removeDuplicates(string s, int k) {

        stack<pair<char, int>> st;

        for (int i = 0; i < s.length(); i++) {

            // New character
            if (st.empty() || st.top().first != s[i]) {
                st.push({s[i], 1});
            }

            // Same character
            else {
                st.top().second++;

                // Remove when count reaches k
                if (st.top().second == k) {
                    st.pop();
                }
            }
        }

        string ans = "";

        // Build answer from stack
        while (!st.empty()) {

            for (int i = 0; i < st.top().second; i++) {
                ans += st.top().first;
            }

            st.pop();
        }

        // Stack gives characters in reverse order
        reverse(ans.begin(), ans.end());

        return ans;
    }
};