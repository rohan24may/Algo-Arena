#include <iostream>
using namespace std;

int main()
{
    int arr[100];
    int n;

    cout << "Enter number of elements of the array: ";
    cin >> n;

    cout << "Enter elements: ";

    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    cout << "Array: ";

    for(int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}