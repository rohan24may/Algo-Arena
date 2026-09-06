#include <iostream>
#include <string>
using namespace std;


class Solution {
    public:
    string remveKdigits(string num,int k){
        string st;

        for(char c :num){
            while(!st.empty() && k>0 && st.back()>c){
                st.pop_back();
                k--;
            }
            st.push_back(c);
        }

        while(k>0){
            st.pop_back();
            k--;
        }

        int i=0;
        while(i<st.size() && st[i]=='0'){
            i++;
        }
        if(i==st.size()){
            return "0";
        }

        return st.substr(i);
    }


};

int main(){
    string num="1432219";
    int k =3;
    Solution s;

    cout<<s.remveKdigits(num,k);
    return 0;

}