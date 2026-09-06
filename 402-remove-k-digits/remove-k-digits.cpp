class Solution {
public:
    string removeKdigits(string num, int k) {
        string st;

        for (int i = 0; i < num.size(); i++) {

            while (!st.empty() && st.back() > num[i] && k > 0) {
                st.pop_back();
                k--;
            }

            st.push_back(num[i]);
        }

        // If removals are still left
        while (k > 0) {
            st.pop_back();
            k--;
        }

        // Remove leading zeros
        int start = 0;

        while (start < st.size() && st[start] == '0') {
            start++;
        }

        // Everything was removed / only zeros
        if (start == st.size()) {
            return "0";
        }

        return st.substr(start);
    }
};