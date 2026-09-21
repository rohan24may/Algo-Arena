#include<iostream>
using namespace std;

const int size=5;
int stack[size];
int top=-1;

bool isFull(int value){
    return top == size -1 ;
}
bool isEmpty(){
    return top = -1 ;
}
void push(int value){
    if(isFull){
        cout<<"Stack is full";
        return;
    }
    top++;
    stack[top] = value;
    cout<<"Element pushed into the stack."
}
void pop(){
    if(isEmpty){
        cout<<"Stack is empty";
        return;
    }
    int value = stack[top];
    top--;

    cout<<"Poped value : "<< value ;
}
void peak(){
        if(isEmpty){
        cout<<"Stack is empty";
        return;
    }
    cout<<"top elemen :"<<stack[top];
}
void diplay(){
             if(isEmpty){
        cout<<"Stack is empty";
        return;
    }

    for(int i = top ; i >= top ; i--){
        cout<<stack[i]<<" ";
    }
}
