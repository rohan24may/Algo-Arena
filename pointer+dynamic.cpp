#include <iostream>
using namespace std;

class Student {
private:
    int marks;

public:
    Student(int m) {
        marks = m;
    }

    void display() {
        cout << "Marks: " << marks;
    }
};

int main() {
    Student *p = new Student(90);

    p->display();

    delete p;

    return 0;
}