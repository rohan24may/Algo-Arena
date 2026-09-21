#include <iostream>
using namespace std;

const int SIZE = 5;

int queue[SIZE];
int front = -1;
int rear = -1;

// Check if queue is empty
bool isEmpty()
{
    return front == -1;
}

// Check if queue is full
bool isFull()
{
    return (rear + 1) % SIZE == front;
}

// Enqueue
void enqueue(int value)
{
    if(isFull())
    {
        cout << "Queue is full\n";
        return;
    }

    // First element
    if(front == -1)
    {
        front = 0;
        rear = 0;
    }
    else
    {
        rear = (rear + 1) % SIZE;
    }

    queue[rear] = value;

    cout << "Element inserted\n";
}

// Dequeue
void dequeue()
{
    if(isEmpty())
    {
        cout << "Queue is empty\n";
        return;
    }

    int value = queue[front];

    // Only one element
    if(front == rear)
    {
        front = -1;
        rear = -1;
    }
    else
    {
        front = (front + 1) % SIZE;
    }

    cout << "Deleted element: " << value << endl;
}

// Peek
void peek()
{
    if(isEmpty())
    {
        cout << "Queue is empty\n";
        return;
    }

    cout << "Front element: " << queue[front] << endl;
}

// Display
void display()
{
    if(isEmpty())
    {
        cout << "Queue is empty\n";
        return;
    }

    cout << "Queue: ";

    int i = front;

    while(true)
    {
        cout << queue[i] << " ";

        if(i == rear)
            break;

        i = (i + 1) % SIZE;
    }

    cout << endl;
}

int main()
{
    int choice;

    do
    {
        cout << "\n----- CIRCULAR QUEUE MENU -----\n";
        cout << "1. Enqueue\n";
        cout << "2. Dequeue\n";
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

                enqueue(value);
                break;
            }

            case 2:
                dequeue();
                break;

            case 3:
                peek();
                break;

            case 4:
                display();
                break;

            case 5:
                if(isEmpty())
                    cout << "Queue is empty\n";
                else
                    cout << "Queue is not empty\n";
                break;

            case 6:
                if(isFull())
                    cout << "Queue is full\n";
                else
                    cout << "Queue is not full\n";
                break;

            case 7:
                cout << "Exiting...\n";
                break;

            default:
                cout << "Invalid choice\n";
        }

    } while(choice != 7);

    return 0;
}