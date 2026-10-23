class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        int currentSum = 0;

        // Calculate the first window's sum
        for (int i = 0; i < k; i++) {
            currentSum += nums[i];
        }

        int maxSum = currentSum;

        // Slide the window
        for (int i = k; i < n; i++) {
            currentSum = currentSum - nums[i - k] + nums[i];
            maxSum = max(maxSum, currentSum);
        }

        return (double)maxSum / k;
    }
};