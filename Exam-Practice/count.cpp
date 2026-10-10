for(int i=0;i<n;i++){
    if(arr[i]==target){
        count++;
    }
    
}
return count ;

#include <iostream>
using namespace std;

int main() {
    int rows = 3, cols = 4;

    int arr[3][4] = {
        {1, 5, 3, 8},
        {2, 9, 4, 6},
        {7, 2, 10, 1}
    };

    int maxElement = arr[0][0];

    for (int i = 0; i < rows * cols; i++) {
        int r = i / cols;
        int c = i % cols;

        if (arr[r][c] > maxElement) {
            maxElement = arr[r][c];
        }
    }

    cout << "Largest element = " << maxElement;

    return 0;
}

// /////////////////////////////////////////////////

void InsertionSort(int arr[],int n){
    for(int i =1; i< n ; i++){
    int key=arr[i];
    int j=i-1;

    while(j>=0 && arr[j]<key){
        arr[j+1]=arr[j];
        j--;
    }
    arr[j+1]=key;
}
}

int main(){
    int arr[]={12,28,45,10,39,18,56,35,40};
    int n=sizeof(arr)/sizeof(arr[0]);

    InsertionSort(arr,n);

    for(int i =0 ;i<n;i++){
        cout<<arr[i]<<" ";
    }
    return 0;

}


///////////////////////////////////////////////////

struct Node{
    int data;
    Node* next;
}
void insertEnd(Node*& head, int value) {
    Node* newNode = new Node{value, nullptr};

    if (head == nullptr) {
        head = newNode;
        return;
    }

    Node* temp = head;

    while (temp->next != nullptr) {
        temp = temp->next;
    }

    temp->next = newNode;
}
int main() {
    Node* head1 = nullptr;
    Node* head2 = nullptr;

    int a[] = {1, 3, 5, 7, 9};
    int b[] = {2, 4, 6, 8};

    for (int x : a)
        insertEnd(head1, x);

    for (int x : b)
        insertEnd(head2, x);
}

////////////////////////


struct Node {
    int data;
    Node* next;
};

Node* merge(Node* head1, Node* head2) {
    Node* head = nullptr;
    Node* tail = nullptr;

    while (head1 != nullptr && head2 != nullptr) {
        Node* selected;

        if (head1->data < head2->data) {
            selected = head1;
            head1 = head1->next;
        }
        else {
            selected = head2;
            head2 = head2->next;
        }

        if (head == nullptr) {
            head = selected;
            tail = selected;
        }
        else {
            tail->next = selected;
            tail = selected;
        }
    }

    if (head1 != nullptr)
        tail->next = head1;
    else
        tail->next = head2;

    return head;
}
//////////////////////////////////////////

Node* merge(Node* head1, Node* head2) {
    Node* head = NULL;
    Node* tail = NULL;

    while (head1 != NULL && head2 != NULL) {
        Node* temp;

        if (head1->data < head2->data) {
            temp = head1;
            head1 = head1->next;
        }
        else {
            temp = head2;
            head2 = head2->next;
        }

        if (head == NULL) {
            head = temp;
            tail = temp;
        }
        else {
            tail->next = temp;
            tail = temp;
        }
    }

    if (head1 != NULL)
        tail->next = head1;
    else
        tail->next = head2;

    return head;
}









/////////////////////////
Node* removeDuplicates(Node* head) {
    Node* temp = head;

    while (temp != NULL) {
        Node* current = temp;

        while (current->next != NULL) {
            if (temp->data == current->next->data) {
                Node* del = current->next;
                current->next = del->next;
                delete del;
            }
            else {
                current = current->next;
            }
        }

        temp = temp->next;
    }

    return head;
}

