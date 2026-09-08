#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {

        vector<int> st;

        for (int a : asteroids) {

            bool alive = true;

            while (!st.empty() && st.back() > 0 && a < 0 && alive) {

                if (abs(st.back()) < abs(a)) {
                    st.pop_back();
                }
                else if (abs(st.back()) == abs(a)) {
                    st.pop_back();
                    alive = false;
                }
                else {
                    alive = false;
                }
            }

            if (alive) {
                st.push_back(a);
            }
        }

        return st;
    }
};

int main(){
    Solution s;
    vector<int> asteroids = {5, 10, -5};
    vector<int> result = s.asteroidCollision(asteroids);

    for (int a : result) {
        cout << a << " ";
    }
    cout << endl;

    return 0;
}