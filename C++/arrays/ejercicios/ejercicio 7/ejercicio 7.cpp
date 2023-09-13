#include<conio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main(){
	
	cout<<"type your name in mayus: "<<endl;
	char name[20];
	cin.getline(name,20,'\n');
	char hola[] = "A";
	
	if(strncmp(name,"A",1)== 0){
		
		strlwr(name);
		cout<<name<<endl;
	}
	else{
		cout<<"the first word is not equal to A";
	}
	
	getch();
	return 0;
}