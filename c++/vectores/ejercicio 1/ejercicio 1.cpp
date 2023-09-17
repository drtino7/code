#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int numbers[] = {1, 2, 3, 4, 5};
	int suma;
	for(int i = 0; i < 5; i++){
	suma += numbers[i];
}
cout<<suma;
	getch();
	return 0;
}