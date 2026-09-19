#include <iostream>
using namespace std;

int main()
{
    int arr[100] = {10, 20, 30, 40, 50};
    int n = 5;
    int position;

    cout << "Enter position of element to insert = ";
    cin >> position;

    int element;
    cout << "Enter element: ";
    cin >> element;

    for(int i = n - 1; i >= position; i--)
    {
        arr[i + 1] = arr[i];
    }

    arr[position] = element;
    n++;

    cout << "Array: ";

    for(int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}