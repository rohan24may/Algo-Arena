class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left=0;
        int right=nums.size()-1;
        int first_indx=-1;
        int second_indx=-1;

        while(left<=right){
            int mid=left+(right-left)/2;

            if(nums[mid]==target){
                first_indx=mid;
                right=mid-1;
            }
            else if(nums[mid]<target){
                left=mid+1;
            }
            else{
                right=mid-1;
            }
        }
        int low=0;
        int high=nums.size()-1;

        while(low<=high){
            int mid=low+(high-low)/2;

            if(nums[mid]==target){
                second_indx=mid;
                low=mid+1;
            }
            else if(nums[mid]>target){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return {first_indx,second_indx};
    }
};