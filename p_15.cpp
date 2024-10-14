#include<iostream>
using namespace std;
class queue
{
 public:
 int front,rear;
 int Q[5];
 int max=5;
 queue()
 {
  front=rear=-1;
 }
 int full();
 int empty();
 void enqueue(int n);
 void dequeue();
 void display();
};

int queue::full()
{
 if(rear==max-1)
 {
  return 1;
 }
 else
 {
  return 0;
 }
}

int queue::empty()
{
 if(front==-1)
 {
  return 1;
 }
 else
 {
  return 0;
 }
}

void queue::enqueue(int n)
{
 if(!full())
 {
  if(front==-1)
  {
   front++;
  }
  rear++;
  Q[rear]=n;
 }
  else
  {
   cout<<"\nQueue overflow!!";
  }
}

void queue::dequeue()
{
 if(!empty())
 {
  if(front==rear)
  {
   cout<<Q[front]<<" Is Deleted";
   front=rear=-1;
  }
  else
  {
   cout<<Q[front]<<" Is Deleted"<<endl;
   front++;
  }
 }
 else
 {
  cout<<"queue Underflow!!";
 }
}

void queue::display()
{
 if(!empty())
 {
  for (int i=front;i<=rear;i++)
  {
   cout<<Q[i]<<" ";
  }
  cout<<"\n";
 }
 else
 {
  cout<<"queue is empty!!";
 }
}
int main()
{
 queue q1;
 int n,choice;
 char ch;
 do
 {
 cout<<"Enter what You want to perform:"<<endl;
 cout<<"1.Insert a new Job \n2.Delete a Job \n3.Display the Jobs"<<endl;
 cout<<"Enter your choice:"<<endl;
 cin>>choice;
 switch(choice)
 {
 case 1:
 {
 do
 {
 cout<<"Enter the job you want to add:"<<endl;
 cin>>n;
 q1.enqueue(n);
 cout<<"Do you want to add more jobs?(y/n)"<<endl;
 cin>>ch;
 }while(ch=='y');
 break;
 }
 
 case 2:
 {
 do
 {
 q1.dequeue();
 cout<<"Do you want to delete more jobs?(y/n)"<<endl;
 cin>>ch;
 }while(ch=='y');
 break;
 }
 case 3:
 {
 cout<<"Jobs=";
 q1.display();
 break;
 }
 
 default:
 cout<<"Invalid Choice!!";
 break;
 }
 cout<<"Do you want to do more operations?(y/n)"<<endl;
 cin>>ch;
 }while(ch=='y');
 return(0);
}



