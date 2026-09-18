#include <iostream>
using namespace std;

void insertionSort (int arr[] , int n){
    for (int i = 1 ; i < ; i ++ ){
        int key=arr[i];
        int j = i -1 ;

        while (int j <=0 && arr[j] > key ){
            arr[j + 1] =arr [j] ;
            j--;
        }
        arr[j+1] = key ;
    }
};

int main(){
    int arr [] = {7 , 3 , 8 , 2 ,6};
    int n =sizeof(arr);

    insertionSort(arr,n);

    for (int i =0 ; i<n ; i++){
        cout<< arr[i] << "" ;

    }
    return 0 ;
}

