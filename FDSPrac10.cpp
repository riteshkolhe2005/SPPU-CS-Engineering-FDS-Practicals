#include <iostream>
#define MAX 20
using namespace std;
class cstack
{
	char str[MAX];
	int top;

public:
	void push(char);
	void pop();
	int isfull();
	int isempty();
	void check();
	cstack()
	{
		top = -1;
	}
};

void cstack::pop()
{
	if (isempty())
		cout << "stack is empty";
	else
		top--;
}

void cstack::check()
{
	char s[20];
	int flag = 0;
	char ch = 'a';
	cout << "Enter the expression:\n";
	cin >> s;
	for (int i = 0; s[i] != '\0'; i++)
	{
		if (s[i] == '(' || s[i] == '{' || s[i] == '[')
		{
			push(s[i]);
		}
		else if (s[i] == ')' || s[i] == '}' || s[i] == ']')
		{

			ch = str[top];
			
			if ((s[i] == ')' && ch == '(') || (s[i] == '}' && ch == '{') || (s[i] == ']' && ch == '['))
			{
				pop();
				flag = 1;
			}
			else
				flag = 0;
		}
	}
	if (isempty() && (flag == 1 || ch == 'a'))
	{
		cout << "Valid";
	}
	else
	{
		cout << "Invalid";
	}
}
void cstack::push(char s)
{
	if (isfull())
		cout << "Stack is full";
	else
	{
		top++;
		str[top] = s;
	}
}
int cstack::isempty()
{
	if (top == -1)
		return 1;
	else
		return 0;
}
int cstack::isfull()
{
	if (top == MAX - 1)
		return 1;
	else
		return 0;
}

int main()
{
	cstack s1;
	s1.check();
	return 0;
}
