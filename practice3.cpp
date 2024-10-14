#include<iostream>
using namespace std;
struct node{
    int data;
    struct node *next;
};
class sea
{
    public:
    struct node *insert();
    void disp(struct node *);
    void intersect(struct node *,struct node *);
    void unio(struct node *,struct node *);
    void diff1(struct node *,struct node *);
    void diff2(struct node *,struct node *);
};
             
struct node* sea::insert()
{
   int n;
   cout<<"enter total no. of students"<<endl;
   cin>>n;
   node *temp,*nn,*start;
   start=NULL;
   for(int i=0;i<n;i++)
   {
        nn=new node;
        cout<<"enter roll number"<<endl;
        cin>>nn->data;
        nn->next=NULL;
        if(start==NULL)
        {
            start=nn;
        }
        else
        {
            temp=start;
            while(temp->next != NULL)
            {
                temp=temp->next;
            }
            temp->next=nn;
        }
        
   } 
   return (start);
}

void sea::intersect(struct node *p,struct node *q)
{
    while(p != NULL)
    {
        while(q != NULL)
        {
            if(p->data==q->data)
            {
                cout<<p->data<<" ";
                break;
            }
            q=q->next;
        }p=p->next;
    }
}

void sea::unio(struct node *p,struct node *q)
{
    struct node *t=p;
    while (t != NULL)
    {
        cout<<t->data<<" ";
        t=t->next;
    }
    for(q;q != NULL ;q=q->next)
    {
        int found=0;
        for(t=p;t != NULL ;t=t->next)
        {
            if(q->data==t->data)
            {
                found=1;
                break;
            }

        }
        if(found==0)
        {
            cout<<q->data<<" ";
        }
    }
}

void sea::diff1(struct node *p,struct node *q)
{
    while(p != NULL)
    {
        struct node *t=q;
        int found=0;
        while(t != NULL)
        {
            if(p->data == t->data)
            {
                found=1;
                break;
            }
            t=t->next;
        }
        if(found==0)
        {
            cout<<p->data<<" ";
        }
        p=p->next;
    }
}

/*void sea::diff2(struct node *p,struct node *q)
{
    while(q != NULL)
    {
        
        int found=0;
        while(p != NULL)
        {
            if(q->data == p->data)
            {
                found=1;
                break;
            }
            p=p->next;
        }
        if(found==0)
        {
            cout<<q->next<<" ";
        }
        q=q->next;
    }
}*/

void sea::disp(struct node *t)
{
    int count=0;
    node *temp=t;
    while(temp!=NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
        count++;
    }
    cout<<"total number of students are "<<count<<endl;
}
int main()
{
    sea obj;
    struct node *head=NULL,*head1=NULL;
    head=obj.insert();
    head1=obj.insert();
    obj.disp(head);
    obj.disp(head1);
    cout<<endl;
    obj.intersect(head,head1);
    cout<<endl;
    obj.unio(head,head1);
    cout<<endl;
    obj.diff1(head,head1);
    cout<<endl;
    obj.diff2(head,head1);

    return 0;
}

