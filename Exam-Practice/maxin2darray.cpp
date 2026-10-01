```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[3][3];

    // Taking input
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "Enter value: ";
            cin >> arr[i][j];
        }
    }

    // Finding maximum
    int max = arr[0][0];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (arr[i][j] > max) {
                max = arr[i][j];
            }
        }
    }

    cout << "Largest element: " << max;

    return 0;
}
```