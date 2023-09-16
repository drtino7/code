#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int number,list[100];
	cout<<"type the number of elemts of the list: "; cin>>number;
	for(int i = 0;i < number;i++){
		cout<<"type the number you want to put on the list"<<endl;
		cin>>list[i];
	}
	for(int i = 0;i < number;i++){
		cout<<list[i]<<endl;
	}
	getch();
	return 0;
}