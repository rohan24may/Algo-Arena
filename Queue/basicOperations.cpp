#include <iostream>
using namespace std;

const int SIZE = 5;

int queue[SIZE];
int front = -1;
int rear = -1;

bool isEmpty()
{
    return front == -1;
}

bool isFull()
{
    return rear == SIZE - 1;
}

void enqueue(int value)
{
    if(isFull())
    {
        cout << "Queue is full\n";
        return;
    }

    if(front == -1)
    {
        front = 0;
    }

    rear++;
    queue[rear] = value;

    cout << "Element inserted\n";
}

void dequeue()
{
    if(isEmpty())
    {
        cout << "Queue is empty\n";
        return;
    }

    int value = queue[front];

    if(front == rear)
    {
        front = -1;
        rear = -1;
    }
    else
    {
        front++;
    }

    cout << "Deleted element: " << value << endl;
}

void peek()
{
    if(isEmpty())
    {
        cout << "Queue is empty\n";
        return;
    }

    cout << "Front element: " << queue[front] << endl;
}

void display()
{
    if(isEmpty())
    {
        cout << "Queue is empty\n";
        return;
    }

    cout << "Queue: ";

    for(int i = front; i <= rear; i++)
    {
        cout << queue[i] << " ";
    }

    cout << endl;
}

int main()
{
    int choice;

    do
    {
        cout << "\n----- QUEUE MENU -----\n";
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