```cpp
#include <iostream>
using namespace std;

int main() {
    int rows, cols;
    cin >> rows >> cols;

    int** arr = new int*[rows];

    for (int i = 0; i < rows; i++) {
        arr[i] = new int[cols];
    }

    int even = 0, odd = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> arr[i][j];

            if (arr[i][j] % 2 == 0)
                even++;
            else
                odd++;
        }
    }

    cout << "Even numbers: " << even << endl;
    cout << "Odd numbers: " << odd << endl;

    for (int i = 0; i < rows; i++) {
        delete[] arr[i];
    }
    delete[] arr;

    return 0;
}
```