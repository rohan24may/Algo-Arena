#include <iostream>
using namespace std;

class Student {
public:
    int marks;

    Student(int m) {
        marks = m;
    }

    void display() {
        cout << marks << endl;
    }
};

int main() {
    Student s1(70);
    Student s2(80);
    Student s3(90);

    s1.display();
    s2.display();
    s3.display();

    return 0;
}