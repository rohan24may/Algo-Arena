#include <iostream>
using namespace std;

class Math {
public:
inline int cube(int x) {
    return x * x * x;
}
};

int main() {
    Math m1;
    m1.cube(30);
}