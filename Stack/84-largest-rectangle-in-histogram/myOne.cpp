#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {

        vector<int> st;
        int maxArea = 0;

        for (int i = 0; i < heights.size(); i++) {

            while (!st.empty() && heights[st.back()] > heights[i]) {

                int top = st.back();
                st.pop_back();

                int height = heights[top];

                int width;

                if (st.empty()) {
                    width = i;
                } else {
                    width = i - st.back() - 1;
                }

                int area = height * width;

                maxArea = max(maxArea, area);
            }

            st.push_back(i);
        }

        // Process remaining bars
        while (!st.empty()) {

            int top = st.back();
            st.pop_back();

            int height = heights[top];

            int width;

            if (st.empty()) {
                width = heights.size();
            } else {
                width = heights.size() - st.back() - 1;
            }

            int area = height * width;

            maxArea = max(maxArea, area);
        }

        return maxArea;
    }
};

int main() {

    Solution s;

    vector<int> heights = {2, 1, 5, 6, 2, 3};

    cout << s.largestRectangleArea(heights);

    return 0;
}