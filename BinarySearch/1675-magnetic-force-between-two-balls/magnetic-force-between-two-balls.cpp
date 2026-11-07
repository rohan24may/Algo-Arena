class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        sort (position.begin(),position.end());

        int n=position.size();
        int low=1;
        int high=position[n-1] -position[0];
        int ans=0;

        while(low<=high){
            int mid=low+(high -low)/2;

            if(canPlace(position,m,mid)){
                ans=mid;
                low=mid+1;
            }
            else{
                high=mid-1;
            }
        }
        return ans;
    }

    bool canPlace(vector<int>&position , int m , int dis){
        int count=1;
        int lastPos=position[0];

        for(int i =1; i<position.size() ; i++){
            if(position[i] - lastPos >= dis){
                count++;
                lastPos=position[i];
            }
        }
        return count>=m;
    }
};

