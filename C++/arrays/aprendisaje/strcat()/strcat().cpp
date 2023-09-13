#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){
	char cat1[] = "hola";
	char cat2[] = " de nuevo";
	char cat3[20];
	
	strcpy(cat3,cat1);
	cout<<cat3<<endl;
	strcat(cat3,cat2);
	cout<<cat3<<endl;	
	
	 
	getch();
	return 0;
}