#include<iostream>
#define MAX 50
using namespace std;
class stack
{
    char str[MAX];
    int top;
    public:
    stack()
    {
        top=-1;
    }
    int isempty();
    int isfull();
    void check();
    void pop();
    char push(char);
};

int stack::isempty()
{
    if(top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int stack::isfull()
{
    if(top == MAX-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void stack::pop()
{
    if(isempty())
    {
        cout<<"stack is empty ";
    }
    else
    {
        top--;
    }
}
char stack::push(char ch)
{
    if(isfull())
    {
        cout<<"stack is full";
    }
    else
    {
        top++;
        str[top]=ch;
    }
}
void stack::check()
{
    char s[50];
    char a='a';
    int flag=0;
    cout<<"enter expression "<<endl;
    cin>>s;
    for(int i=0;s[i] != '\0';i++)
    {
        if(s[i]=='(' || s[i]=='{' || s[i]=='[')
        {
            push(s[i]);
        }
        else if(s[i]==')' || s[i]==']' || s[i]=='}')
        {
            a=str[top];
            if((s[i]==')' && a=='(') || (s[i]==']' && a=='[') || (s[i]=='}' && a=='{'))
            {
                pop();
                flag=1;
            }
            else
            {
                flag=0;
            }
        }
    }
    if (isempty() && (flag==1 || a=='a'))
    {
        cout<<"valid";
    }
    else
    {
        cout<<"invalid";
    }
}
int main()
{
    stack obj;
    obj.check();
    return 0;
}