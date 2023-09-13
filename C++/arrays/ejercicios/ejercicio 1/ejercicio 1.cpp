//ejercicio 1;
#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){
	
	char name[10];
	cout<<"type your name: "; cin.getline(name,20,'\n');
	int name_lenght = strlen(name);
	
	
	if(name_lenght <= 10){
		cout<<name<<endl;
	}
	else{
		cout<<"the name typed has more than ten caracters"<<endl;
	}
	
	
	getch();
	return 0;
}