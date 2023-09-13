//serie de fibonacci
#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int n,s_f,a = 1,b = 1,c;
	cout<<"digite un numero: "<<endl; cin>>n;
	
	for(int i = 0;i < n;i++){
		
		c =  a + b;
		a = b;
		b = c;
		
		if(i == 0){
			cout<<"1,";	
		}	
		
	 	cout<<c;
	 	if((i+1) < n){
	 		cout<<",";
		}
	}
	getch();
	return 0;	
}