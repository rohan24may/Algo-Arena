#include <iostream>
using namespace std;

int main()
{
    int arr[10][10];
    int rows, cols;

    cin >> rows >> cols;

    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < cols; j++)
        {
            cin >> arr[i][j];
        }
    }

    cout << "Transpose:\n";

    for(int j = 0; j < cols; j++)
    {
        for(int i = 0; i < rows; i++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}