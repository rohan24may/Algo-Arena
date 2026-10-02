///single/

void deleteBeginning() {
    if (head == NULL) {
        return;
    }

    // Only one node
    if (head == tail) {
        delete head;
        head = NULL;
        tail = NULL;
        return;
    }

    // Multiple nodes
    Node* temp = head;
    head = head->next;
    tail->next = head;
    delete temp;
}

//

Node* temp = tail;
Node* current = head;

while (current->next != tail) {
    current = current->next;
}

current->next = head;
tail = current;
delete temp;