#include<iostream>
#include<cstdlib>
using namespace std;

class PizzaParlor {
    int front, rear, orders[5];

public:
    PizzaParlor() {
        front = -1;
        rear = -1;
    }

    int isFull() {
        if ((front == 0 && rear == 4) || front == (rear + 1) % 5) {
            return 1;
        } else {
            return 0;
        }
    }

    int isEmpty() {
        if (front == -1 && rear == -1) {
            return 1;
        } else {
            return 0;
        }
    }

    void addOrder() {
        if (isFull() == 0) {
            cout << "\nEnter the Pizza ID: ";
            if (front == -1 && rear == -1) {
                front = 0;
                rear = 0;
                cin >> orders[rear];
            } else {
                rear = (rear + 1) % 5;
                cin >> orders[rear];
            }
            char c;
            cout << "Do you want to add another order? ";
            cin >> c;
            if (c == 'y' || c == 'Y') {
                addOrder();
            }
        } else {
            cout << "\nOrders are full.";
        }
    }

    void serveOrder() {
        if (isEmpty() == 0) {
            if (front == rear) {
                cout << "\nOrder served is: " << orders[front];
                front = -1;
                rear = -1;
            } else {
                cout << "\nOrder served is: " << orders[front];
                front = (front + 1) % 5;
            }
        } else {
            cout << "\nOrders are empty.";
        }
    }

    void displayOrders() {
        if (isEmpty() == 0) {
            for (int i = front; i != rear; i = (i + 1) % 5) {
                cout << orders[i] << "<-";
            }
            cout << orders[rear];
        } else {
            cout << "\nOrders are empty";
        }
    }

    void processChoice() {
        int choice;
        cout << "\n\n* * * * PIZZA PARLOUR * * * *\n\n";
        cout << "1. Add a Pizza\n2. Display the Orders\n3. Serve a Pizza\n4. Exit\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                addOrder();
                break;
            case 2:
                displayOrders();
                break;
            case 3:
                serveOrder();
                break;
            case 4:
                exit(0);
            default:
                cout << "Invalid choice";
                processChoice();
        }

        char ch;
        cout << "\nDo you want to continue? ";
        cin >> ch;
        if (ch == 'y' || ch == 'Y') {
            processChoice();
        }
    }
};

int main() {
    PizzaParlor pizzaParlor;
    pizzaParlor.processChoice();
    return 0;
}

