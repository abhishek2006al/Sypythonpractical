#include <iostream>
using namespace std;

struct Node {
    int empId;
    string empName;
    float salary;
    Node *next;
};

Node *head = NULL;

void insert() {
    Node *newNode = new Node;

    cout << "Enter Employee Id: ";
    cin >> newNode->empId;

    cout << "\nEnter Employee name: ";
    cin >> newNode->empName;

    cout << "\nEnter Employee salary: ";
    cin >> newNode->salary;

    newNode->next = head;
    head = newNode;

    cout << "\nEmployee record inserted successfully.";
}

void deleteNode(int id) {

    if (head == NULL) {
        cout << "\nList is empty..";
        return;
    }

    Node *temp = head;
    Node *prev = NULL;

    // Delete first node
    if (head->empId == id) {
        head = head->next;
        delete temp;

        cout << "\nEmployee record Deleted Successfully.";
        return;
    }

    // Search for the node
    while (temp != NULL && temp->empId != id) {
        prev = temp;
        temp = temp->next;
    }

    // Employee not found
    if (temp == NULL) {
        cout << "\nEmployee record not found.";
        return;
    }

    // Delete node
    prev->next = temp->next;
    delete temp;

    cout << "\nEmployee record Deleted Successfully.";
}

void search(int id) {
    Node *temp = head;

    while (temp != NULL) {
        if (temp->empId == id) {
            cout << "\nEmployee Found.";
            cout << "\nEmployee Id: " << temp->empId;
            cout << "\nEmployee name: " << temp->empName;
            cout << "\nEmployee salary: " << temp->salary;
            return;
        }

        temp = temp->next;
    }

    cout << "\nEmployee record not found.";
}

void display() {
    if (head == NULL) {
        cout << "\nList is empty";
        return;
    }

    Node *temp = head;

    cout << "\nEmployee Records";
    cout << "\n======================================================";

    while (temp != NULL) {
        cout << "\nEmployee Id: " << temp->empId;
        cout << "\nEmployee name: " << temp->empName;
        cout << "\nEmployee salary: " << temp->salary;
        cout << "\n------------------------------------------------------";

        temp = temp->next;
    }
}

int main() {
    int choice, id;

    do {
        cout << "\n\n*************************** Employee Record Management **************************";
        cout << "\n1. Insert Employee";
        cout << "\n2. Delete Employee";
        cout << "\n3. Search Employee";
        cout << "\n4. Display Employee";
        cout << "\n5. Exit";
        cout << "\nEnter choice: ";
        cin >> choice;

        switch (choice) {

            case 1:
                insert();
                break;

            case 2:
                cout << "\nEnter employee id to delete: ";
                cin >> id;
                deleteNode(id);
                break;

            case 3:
                cout << "\nEnter employee id to search: ";
                cin >> id;
                search(id);
                break;

            case 4:
                display();
                break;

            case 5:
                cout << "\nProgram End";
                break;

            default:
                cout << "\nInvalid choice";
        }

    } while (choice != 5);

    return 0;
}