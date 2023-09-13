#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int numbers[] = {1,5,10},multiplication = 1;
	for(int i = 1;i < 3;i++){
	multiplication = multiplication * numbers[i];
 }
 cout<<multiplication;
	getch();
	return 0;
}