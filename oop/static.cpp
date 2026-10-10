#include <iostream>
using namespace std;

class Student {
private:
    int marks;

public:
    static int count;

    Student() {
        count++;
    }

    static void display() {
        cout << "Counts are: " << count;
    }
};
    
int Student::count = 0;

int main() {
    Student s1;
    Student s2;

    Student::display();

    return 0;
}