bool search(Node* hed ,int target){
    Node* temp=head;

    while(temp!=null){
        if(temp->data==target){
            return true;
        }
        temp=temp->next;
    }
    return false;
}