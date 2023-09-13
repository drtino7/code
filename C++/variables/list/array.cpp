#include<iostream>
#include<string.h>
using namespace std;
int main(){

//way number:1

int array[10] = {0,1,2,3,4,5,6,7,8,9} ;

for(int i = 0; i < 10; i++){

cout<<"your number is: "<<array[i]<<"\n";
}

char name[20];
//way number: 2
cout<<"type your name: ";
cin>>name; 
cout<<name<<endl;

//way number: 3
cout<<"type your name: "; 
cin.getline(name,5,'\n');
cout<<name;

return 0;
}
