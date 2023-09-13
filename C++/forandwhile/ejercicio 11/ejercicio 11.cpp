#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;
int main(){
	int num,res,suma;
	cout<<"digite un numero: "<<endl; cin>>num;
	for(int i = 1;i <= num;i++){
		res = pow(2,i);
		 suma +=ç res; 
	}
	cout<<suma;
	getch();
	return 0;
}