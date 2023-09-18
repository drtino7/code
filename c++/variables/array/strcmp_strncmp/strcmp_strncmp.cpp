//compere if they are equal or which is bigger alfabetic
#include<iostream>
#include<string.h>
using namespace std;
int main(){
	
	char array[] = "valentino";
	char arrayb[] = "valentino";
	
	if(strcmp(array,arrayb) == 0){
		cout<<"is the same"<<endl;
	}
	else{
		cout<<"is not the same"<<endl;
		
	}
	

	 char arrayc[] = "plane";
	 char arrayd[] = "boat";
	if(strcmp(array,arrayb) > 0){
		cout<<arrayc<<" is major than "<<arrayd<<endl;
	}
	else{
		cout<<arrayd<<" is major than "<<arrayc<<endl;
	}
	cout<<"///////////////////////////////////////////////////////////////////////////////////////////////////"<<endl;
	char word1[] = "hi";
	char word2[] = "icecream";
	if(strncmp(word1,word2,1)== 0){
		cout<<"the firts letter is equal";
	}
	else{
		
		cout<<"the first letter is not equal ";
		
	}

	return 0;
}
