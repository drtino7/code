#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){
	char nombre[20],nombreb[20];
	
	 cout<<"type your name: "<<endl;
	cin.getline(nombre,20,'\n');
	
	strcpy(nombreb,nombre);

	cout<<nombre;
	getch();
	return 0;
}