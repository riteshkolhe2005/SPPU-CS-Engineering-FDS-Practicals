#include<iostream>
#define max 10
using namespace std;
class cqueue{
    int q[max];
    int rear,front;
    public:
        void dequeue();
        void enqueue(int);
        void display();
    cqueue()
    {
        front=rear=-1;
    } 

};

void cqueue::enqueue(int x){
    if(rear==max-1)
        cout<<"queue is full";
    else if(rear==-1 && front==-1){
        rear=front=0;
        q[rear]=x;
    }
    else{
        rear++;
        q[rear]=x;
    }
}
void cqueue::dequeue()
{
    if(front==-1 && rear==-1)
        cout<<"queue is empty";
    else if(front==rear)
        rear=front=-1;
    else{
        cout<<q[front];
        front++;
    }
}
void cqueue::display()
{
    if(rear==-1 && front==-1)
        cout<<"queue is empty";
    else{
        for(int i=front;i<rear+1;i++)
        {
            cout<<q[i];
        }
        cout<<endl;
    }
}
int main(){
    cqueue c;
    int ch,x;
    while(ch!=4)
    {
        switch(ch)
        {
            case 1:  cout<<"enter job id";
                     cin>>x;
                     c.enqueue(x);
                     break;
            case 2: c.dequeue();
                    break;
            case 3: c.display();
                    break;
            case 4: cout<<"\n exit";
                    break;
            default: cout<<"Invalid";
                     break;
        }
        cout<<"\n 1.enqueue job\n 2.dequeue job\n 3.display job\n 4.exit\n Enter your choice";
        cin>>ch;
        
    }
    return 0;
}