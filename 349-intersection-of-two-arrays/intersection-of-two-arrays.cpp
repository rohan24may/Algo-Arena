class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> st;
        unordered_set<int> result;

        for(int i=0 ; i<nums1.size() ; i++){
            st.insert(nums1[i]);
        }

        for(int j =0 ; j<nums2.size() ; j++){
            if(st.find(nums2[j]) != st.end()){
                result.insert(nums2[j]);
            }
        }

        vector<int>ans;

        for(int x : result){
            ans.push_back(x);
        }
        return ans;
    }
};