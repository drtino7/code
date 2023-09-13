#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){

	char cat[] = "hello whats up: ";
	char name[20];
	cout<<"type your name: ";
	cin.getline(name,20,'\n');
	cout<<endl;
	strcat(cat,name); 

	cout<<name;
	 
	getch();
	return 0;
}