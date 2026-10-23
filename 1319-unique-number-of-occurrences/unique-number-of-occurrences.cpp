class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> mp;

        for (int num : arr) {
            mp[num]++;
        }

        unordered_set<int> seen;

        for (auto pair : mp) {
            if (seen.find(pair.second) != seen.end()) {
                return false;
            }

            seen.insert(pair.second);
        }

        return true;
    }
};