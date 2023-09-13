#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int n, r = 0;
	cout<<"digite un numero: "<<endl; cin>>n;
	for(int i = 0;i < n;i++)
	if(i % 2 == 0){
		r = r + i;
	}
	else{
		r = r - i;
	}
	cout<<"el resultado es: "<<r<<endl;
	getch();
	return 0;
}