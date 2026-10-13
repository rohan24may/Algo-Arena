class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char,int>mp;

        for(int i=0 ; i<text.length() ; i++){
            mp[text[i]] ++ ;
        }

        int ans = min(mp['b'], mp['a']);
        ans = min(ans, mp['l'] / 2);
        ans = min(ans, mp['o'] / 2);
        ans = min(ans, mp['n']);

        return ans;
    }
};