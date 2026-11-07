class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sptr=0;
        int tptr=0;

        while(sptr<s.length() && tptr<t.length()){
            if(s[sptr] == t[tptr]){
                sptr++;
            }
            tptr++;
        }
        return sptr==s.length();
        
    }
};