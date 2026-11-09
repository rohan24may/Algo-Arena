class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int up = 0;
        int down = 0;
        int maxLen = 0;

        for (int i = 1; i < arr.size(); i++) {

            // New mountain starts after descending
if (arr[i] > arr[i - 1] && down > 0) {
    if (up > 0) {
        maxLen = max(maxLen, up + down + 1);
    }

    up = 0;
    down = 0;
}

            // Equal elements break the mountain
            if (arr[i] == arr[i - 1]) {
                up = 0;
                down = 0;
            }
            // Uphill
            else if (arr[i] > arr[i - 1]) {
                up++;
            }
            // Downhill
            else {
                down++;
            }

            // Update longest valid mountain
            if (up > 0 && down > 0) {
                maxLen = max(maxLen, up + down + 1);
            }
        }

        return maxLen;
    }
};