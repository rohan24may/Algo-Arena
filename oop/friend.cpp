#include <iostream>
using namespace std;

class Student {
private:
    int marks;

public:
    Student(int x) {
        marks = x;
    }

    friend void display(Student s);
};

void display(Student s) {
    cout << s.marks;
}

int main() {
    Student s1(90);

    display(s1);

    return 0;
}