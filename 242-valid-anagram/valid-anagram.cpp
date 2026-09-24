class Solution {
public:
    bool isAnagram(string s, string t) {

        if(s.length() != t.length()){
            return false;
        }

        unordered_map<char, int> mp;

        // Count characters in s
        for(char c : s){
            mp[c]++;
        }

        // Check characters in t
        for(int i = 0; i < t.length(); i++){

            if(mp.find(t[i]) == mp.end() || mp[t[i]] == 0){
                return false;
            }

            mp[t[i]]--;
        }

        return true;
    }
};