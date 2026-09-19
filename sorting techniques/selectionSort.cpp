#include <iostream>
using namespace std ;

void selection(int arr[] , int n ){
    for (int i = 0 ; i<n-1 ; i++){
        int minInex= i ;
        for(int j = i+1 ; j < n ; j++){
            if(arr[j] < arr[minInex]){
                minInex=j;
            }
        }
        int temp = arr[i]; 
        arr[i]=arr[minInex];
        arr[minInex]=temp;

    }
}
int main(){
    int arr[]= {7,3,4,5,2,9};
    int n = sizeof(arr)/sizeof(arr[0]);

    selection(arr,n);

    for (int i =0 ; i<n ; i++){
        cout<<arr[i]<<" ";
    }
}