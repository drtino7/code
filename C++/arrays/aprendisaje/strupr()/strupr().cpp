//strupr()  pasa minusculas a mayusculas
#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){
	
	char nombre[] = "Valentino";
	
	strupr(nombre);
	cout<<nombre<<endl;
	
	getch();
	return 0;
}