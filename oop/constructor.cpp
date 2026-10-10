#include <iostream>
using namespace std;

class Student {
public:
    int marks;

    Student(){
        cout<<"Default";
    }

    Student(int m) {
        marks = m;
        cout<<"Marks"<<marks;
    }

};

int main() {
    Student s1;
    Student s2(80);
}