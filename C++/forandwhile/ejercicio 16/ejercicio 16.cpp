#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int number,equation;
	cout<<"type a number to descompose: "<<endl; cin>>number;
    for(int i = 2;number > 1;i++){
    	while(number % i == 0)
    		number /= i,
    		cout<<i<<" "<<endl;
	}
	getch();
	return 0;
}
