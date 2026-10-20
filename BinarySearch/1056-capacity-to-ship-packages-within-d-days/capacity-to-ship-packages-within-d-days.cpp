class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int left=*max_element(weights.begin() , weights.end());
        int right =accumulate(weights.begin(),weights.end(),0);

        while(left<right){
            int mid=left+(right-left)/2;

            int daysNeeded = 1;
            int currentLoad=0;

            for(int i =0 ;i<weights.size() ;i++){
                if(currentLoad+weights[i] > mid){
                    daysNeeded++;
                    currentLoad=weights[i];
                }
                else{
                    currentLoad+=weights[i];
                }
            }

            if(daysNeeded <= days){
                right=mid;
            }
            else{
                left=mid+1;
            }
        }
        return left;
    }
};