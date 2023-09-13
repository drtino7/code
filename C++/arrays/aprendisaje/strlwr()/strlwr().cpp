//strlwr() pasa mayusculas a minusculas
#include<conio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main(){
	
	char mayus[] = "HELLO WORLD!";
	strlwr(mayus);
	
	cout<<mayus<<endl;
	getch();
	return 0;
}