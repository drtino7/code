#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){
	
	char word [20];
	cout<<"type a word to check if it is polyndroma: ";
	cin.getline(word,20,'\n');
	char copy[20];
	strcpy(copy,word);
	strrev(copy);
	
	cout<<copy<<endl;
	cout<<word<<endl;
	
	if(strcmp(copy,wordhi) == 0){
		cout<<"the typed word is polyndroma";
	}
	else{
		cout<<"the word isnt polyndroma";
	}
	
	getch();
	return 0;
}