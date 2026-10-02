Node* newNode=new Node(5);

newNode->next=head;
head->prev=newNode;
head=newNode;

//end/;

Node* newNode = new Node(40);
    newNode->next = NULL;
    tail->next = newNode;
    newNode->prev = tail;
    tail = newNode;

   //

Node* newNode = new Node(40);

if (head == NULL) {
    head = tail = newNode;
}
else {
    tail->next = newNode;
    newNode->prev = tail;
    tail = newNode;
}

//

Node* temp=head;
head=head->next;
head->prev=null;
delete temp;

//
if (head == NULL) {
    return;
}

Node* temp = head;
head = head->next;

if (head != NULL) {
    head->prev = NULL;
}

delete temp;

//

void deleteEnd() {
    if (head == NULL) {
        return;
    }

    // Only one node
    if (head->next == NULL) {
        delete head;
        head = NULL;
        tail = NULL;
        return;
    }

    // Multiple nodes
    Node* temp = tail;
    tail = tail->prev;
    tail->next = NULL;
    delete temp;
}