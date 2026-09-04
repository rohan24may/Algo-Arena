#include <iostream>
#include <vector>
using namespace std;

class MergeSort {

private:

    void merge(int arr[], int low, int mid, int high) {

        vector<int> temp;

        int i = low;
        int j = mid + 1;

        while (i <= mid && j <= high) {

            if (arr[i] < arr[j]) {
                temp.push_back(arr[i]);
                i++;
            }
            else {
                temp.push_back(arr[j]);
                j++;
            }
        }

        while (i <= mid) {
            temp.push_back(arr[i]);
            i++;
        }

        while (j <= high) {
            temp.push_back(arr[j]);
            j++;
        }

        for (int k = 0; k < temp.size(); k++) {
            arr[low + k] = temp[k];
        }
    }


    void mergeSort(int arr[], int low, int high) {

        if (low < high) {

            int mid = (low + high) / 2;

            mergeSort(arr, low, mid);

            mergeSort(arr, mid + 1, high);

            merge(arr, low, mid, high);
        }
    }


public:

    void sort(int arr[], int low, int high) {
        mergeSort(arr, low, high);
    }
};


int main() {

    int arr[] = {12, 11, 13, 5, 6, 7};

    int n = sizeof(arr) / sizeof(arr[0]);

    MergeSort ms;

    ms.sort(arr, 0, n - 1);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}