#include <iostream>
using namespace std;

namespace A {
    int x = 20;
}

namespace B {
    int x = 30;
}

int main() {
    cout << "A is " << A::x << endl;
    cout << "B is " << B::x << endl;
}