#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){
	
	char word1[20], word2[20];
	
	cout<<"type a word: ";
	cin.getline(word1,20,'\n');
	
	cout<<"type a word: ";
	cin.getline(word2,20,'\n');
	
	strupr(word1);
	strupr(word2);
	
	cout<<"the word are: "<<word1<<" and "<<word2<<endl;
	
	if(strcmp(word1,word2) == 0){
		
		cout<<"the are the same word"<<'\n';
	}
	else{
		
		cout<<"there arent the same word"<<'\n';
	}
	getch();
	return 0;
}