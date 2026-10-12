class Solution {
public:
    bool wordPattern(string pattern, string s) {

        unordered_map<char, string> mp1;
        unordered_map<string, char> mp2;

        stringstream ss(s);
        string word;
        int i = 0;

        while (ss >> word) {

            if (i >= pattern.length()) {
                return false;
            }

            // Check character -> word mapping
            if (mp1.find(pattern[i]) != mp1.end() &&
                mp1[pattern[i]] != word) {
                return false;
            }

            // Check word -> character mapping
            if (mp2.find(word) != mp2.end() &&
                mp2[word] != pattern[i]) {
                return false;
            }

            // Store both mappings
            mp1[pattern[i]] = word;
            mp2[word] = pattern[i];

            i++;
        }

        // Check whether the number of words matches the pattern length
        return i == pattern.length();
    }
};