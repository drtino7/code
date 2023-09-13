#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){
char worda[30],wordb[30];
cout<<"type the first word: "; cin.getline(worda,30,'\n');	cout<<endl;
cout<<"type the second word: "; cin.getline(wordb,30,'\n');	cout<<endl;
	
if(strcmp(worda,wordb) == 0){
	cout<<"the word is the same"<<endl;
}
else if(strcmp(worda,wordb) > 0){
	cout<<worda<<" is major than "<<wordb<<endl;
}
else{
	cout<<wordb<<" is major than "<<worda<<endl;
}



	getch();
	return 0;
}