#include<iostream>
#include<conio.h>
#include<stdlib.h>
using namespace std;
int main(){
	
	char FLOAT[20];
	char INT[20];
	float FLOAT2;
	int INT2;
	float sum;
	
	cout<<"tipe a float: ";
	cin.getline(FLOAT,20,'\n');
	cout<<'\n'<<"tipe a INTEGER: ";
	cin.getline(INT,20,'\n');
	
	FLOAT2 = atof(FLOAT);
	INT2 = atoi(INT);
	
	cout<<"your nambers are: "<<FLOAT2<<" and "<<INT2<<endl;
	
	sum = FLOAT2 + INT2;
	
	cout<<"the result is: "<<sum;
	
	getch();
	return 0;
}