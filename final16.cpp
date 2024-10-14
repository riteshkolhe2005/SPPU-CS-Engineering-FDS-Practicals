#include<iostream>
#define q 10
using namespace std;
struct node{
    int data;
    struct node*next;
};
struct node* front=0;
struct node* rear=0;
class cqueue{
  public:
    void addjob(int);
    void deletejob();
    void display();
};
void cqueue::addjob(int n)
{
    node *nn;
    cout<<"enter job id:"<<endl;
    cin>>n;
    nn=new node;
    nn->next=NULL;
    nn->data=n;
    if(front==NULL && rear==NULL)
        front=rear=nn;
    else{
        rear->next=nn;
        rear=nn;
    }
        
}
void cqueue::display()
{
    node *temp;
    if(rear==0 && front==0)
        cout<<"queue is empty";
    else{
        temp=front;
        while(temp!=NULL){
            cout<<temp->data<<endl;
            temp=temp->next;
        }
    }
}
void cqueue::deletejob()
{
    node *temp; 
    if(front==0 && rear==0)
        cout<<"queue is empty";
    else{
        temp=front;
        front=front->next;
        delete(temp);
    }
}
int main(){
  int n,choice=0;
  cqueue c;
  while(choice!=4){
    cout<<"\n 1.addjob\n 2.deletejob\n 3.display job\n 4.exit\n enter your choice:"<<endl;
    cin>>choice;
    switch(choice){
        case 1: c.addjob(n);
                break;
        case 2: c.deletejob();
                break;
        case 3: c.display();
                break;
        case 4: cout<<"\n exit";
                break;
        default: 
                 cout<<"Invalid";
                 break;
    }
   
  }

    return 0;
}