class Solution {
public:
    string simplifyPath(string path) {
        vector<string>st;
        string part;

        stringstream ss(path);

        while(getline(ss,part,'/')){
            if (part==".."){
                if(!st.empty()){
                    st.pop_back();
                }
            }
            else if(part=="."){
                continue;
            }
            else if(part!=""){
                st.push_back(part);
            }
        }

        if (st.empty()){
            return "/";
        }

        string ans = "";

        for (int i = 0 ; i<st.size() ; i++){
            ans += "/"+st[i];
        }

        return ans ;
        
    }
};