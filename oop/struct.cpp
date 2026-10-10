#include <iostream>
using namespace std;

struct Student {
    int roll;
    int marks;
    int age;
    

    void input() {
        cout << "Enter roll no, marks and age: ";
        cin >> roll >> marks >> age;
    }

    void display() {
        cout << "Roll No: " << roll << endl;
        cout << "Marks: " << marks << endl;
        cout << "Age: " << age << endl;
    }
};

int main() {
    Student s1;

    s1.input();
    s1.display();

    return 0;
}