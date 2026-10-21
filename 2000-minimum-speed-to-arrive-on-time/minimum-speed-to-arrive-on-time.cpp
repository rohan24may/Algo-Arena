
class Solution {
public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        int left = 1;
        int right = 10000000;

        while (left < right) {
            int mid = left + (right - left) / 2;
            double totalTime = 0;

            for (int i = 0; i < dist.size(); i++) {
                if (i == dist.size() - 1) {
                    // Last train: exact travel time
                    totalTime += (double)dist[i] / mid;
                } else {
                    // Other trains: round up to the next hour
                    totalTime += ceil((double)dist[i] / mid);
                }
            }

            if (totalTime <= hour) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        // Check whether the minimum possible speed works
        double totalTime = 0;

        for (int i = 0; i < dist.size(); i++) {
            if (i == dist.size() - 1) {
                totalTime += (double)dist[i] / left;
            } else {
                totalTime += ceil((double)dist[i] / left);
            }
        }

        if (totalTime <= hour) {
            return left;
        }

        return -1;
    }
};
