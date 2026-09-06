class Solution {
public:
    string simplifyPath(string path) {

        vector<string> st;
        string part;

        // Split path using '/'
        stringstream ss(path);

        while (getline(ss, part, '/')) {

            // Parent directory
            if (part == "..") {

                if (!st.empty()) {
                    st.pop_back();
                }
            }

            // Current directory
            else if (part == ".") {
                continue;
            }

            // Normal directory
            else if (part != "") {
                st.push_back(part);
            }
        }

        // If nothing is left, we are at root
        if (st.empty()) {
            return "/";
        }

        // Build final path
        string ans = "";

        for (int i = 0; i < st.size(); i++) {
            ans += "/" + st[i];
        }

        return ans;
    }
};