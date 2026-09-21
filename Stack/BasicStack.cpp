#include <iostream>
using namespace std;

const int SIZE = 5;

int stack[SIZE];
int top = -1;

// Check if stack is empty
bool isEmpty()
{
    return top == -1;
}

// Check if stack is full
bool isFull()
{
    return top == SIZE - 1;
}

// Push
void push(int value)
{
    if(isFull())
    {
        cout << "Stack Overflow\n";
        return;
    }

    top++;
    stack[top] = value;

    cout << "Element pushed.\n";
}

// Pop
void pop()
{
    if(isEmpty())
    {
        cout << "Stack is empty.\n";
        return;
    }

    int value = stack[top];
    top--;

    cout << "Deleted element: " << value << endl;
}

// Peek
void peek()
{
    if(isEmpty())
    {
        cout << "Stack is empty.\n";
        return;
    }

    cout << "Top element: " << stack[top] << endl;
}

// Display
void display()
{
    if(isEmpty())
    {
        cout << "Stack is empty.\n";
        return;
    }

    cout << "Stack: ";

    for(int i = top; i >= 0; i--)
    {
        cout << stack[i] << " ";
    }

    cout << endl;
}

int main()
{
    int choice;

    do
    {
        cout << "\n----- STACK MENU -----\n";
        cout << "1. Push\n";
        cout << "2. Pop\n";
        cout << "3. Peek\n";
        cout << "4. Display\n";
        cout << "5. IsEmpty\n";
        cout << "6. IsFull\n";
        cout << "7. Exit\n";

        cout << "Enter choice: ";
        cin >> choice;

        switch(choice)
        {
            case 1:
            {
                int value;

                cout << "Enter value: ";
                cin >> value;

                push(value);
                break;
            }

            case 2:
                pop();
                break;

            case 3:
                peek();
                break;

            case 4:
                display();
                break;

            case 5:
                if(isEmpty())
                    cout << "Stack is empty.\n";
                else
                    cout << "Stack is not empty.\n";
                break;

            case 6:
                if(isFull())
                    cout << "Stack is full.\n";
                else
                    cout << "Stack is not full.\n";
                break;

            case 7:
                cout << "Exiting...\n";
                break;

            default:
                cout << "Invalid choice.\n";
        }

    } while(choice != 7);

    return 0;
}