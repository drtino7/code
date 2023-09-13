//aprendisaje 2  copiar contenido funcion strcpy()
#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){
	char nombre[] = "valentino";
	char nombreb[20];
	
	strcpy(nombreb,nombre);
	
	cout<<nombre;
	
getch();
return 0;
}