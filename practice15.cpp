#include<iostream>
using namespace std;
#define max 50
class queue{
    public:
    int rear,front;
    int q[max];
    queue()
    {
        rear=front=-1;
    }
    void enqueue(int);
    void dqueue();
    void disp();
};

void queue::enqueue(int x)
{
    if(rear==max-1)
    {
        cout<<"queue is full"<<endl;
    }
    else if(rear==-1 && front==-1)
    {
        front=rear=0;
        q[rear]=x;
    }
    else
    {
        rear++;
        q[rear]=x;
    }

}

void queue::dqueue()
{
    if(front==-1 && rear==-1)
    {
        cout<<"queue is empty"<<endl;
    }
    else if(front==rear)
    {
        front=rear=-1;
    }
    else{
        cout<<q[front];
        front++;
    }
}

void queue::disp()
{
    if(front==-1 && rear==-1)
    {
        cout<<"queue is empty"<<endl;
    }
    else{
        for(int i=front;i<rear+1;i++)
        {
            cout<<q[i]<<" ";
        }
    }
}

int main()
{
    queue obj;
    int ch,x;
    char s;
    do
    {
        cout<<"1.add job\n2.delete job\n3.display\n4.exit";
        cin>>ch;
        switch(ch)
        {
            case 1:
                cout<<"enter job :";
                cin>>x;
                obj.enqueue(x);
                break;
            case 2:
                obj.dqueue();
                break;
            case 3:
                obj.disp();
                break;
            case 4:
                break;
            default:
                cout<<"invalid input "<<endl;
        }
        cout<<"do you want to continue (y/n) :";
        cin>>s;

    }while(s=='y');
    return 0;
}