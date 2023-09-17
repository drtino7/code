//aprendisaje 2  copiar contenido funcion strcpy()
#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){
	char name[] = "valentino";
	char nameb[20];
	
	strcpy(nameb,name);
	
	cout<<name;
	
getch();
return 0;
}