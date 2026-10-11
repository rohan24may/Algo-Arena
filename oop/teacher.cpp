#include <iostream>
using namespace std;

class Student {
private:
    int marks;

public:
    Student(int m) {
        marks = m;
    }

    friend class Teacher;
};

class Teacher {
public:
    void display(Student s) {
        cout << s.marks;
    }
};

int main() {
    Student s1(90);

    Teacher t;
    t.display(s1);

    return 0;
}