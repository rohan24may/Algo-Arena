class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char,int>mp;

        for(int i=0;i<s.length() ; i++){
            mp[s[i]]++;
        }
        int length=0;

        for(auto p : mp){
            length += (p.second / 2) * 2;
        }

        for(auto p : mp){
            if(p.second % 2 !=0){
                length++;
                break;
            }
        }

        return length ;
        
    }
};