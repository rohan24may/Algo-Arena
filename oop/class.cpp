#include <iostream>
using namespace std;

class Student {
private:
    string name;
    int marks;

public:
    void input() {
        cout << "Enter Name and marks: ";
        cin >> name >> marks;
    }

    void display() {
        cout << "Name: " << name << endl;
        cout << "Marks: " << marks << endl;
    }
};

int main() {
    Student s1, s2;

    s1.input();
    s2.input();

    s1.display();
    s2.display();

    return 0;
}