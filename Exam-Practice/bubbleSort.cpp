#include <iostream>
using namespace std;

void Bubblesort(int arr[] ,int n){
    for(int i = 0 ; i <n-1 ; i++){
        for(int j=0 ; j < n-i-1 ; j++){
            if(arr[j] > arr[j+1]){
                int temp =arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
};

int main(){
    int arr[]={2,4,2,4,5,5,3};
    int n=sizeof(arr)/sizeof(arr[0]);

    Bubblesort(arr,n);

    for(int i=0;i<n ; i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}