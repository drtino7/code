//compara si son iguales o el pocisionamiento en el alfabeto
#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
int main(){
	
	char array[] = "valentino";
	char arrayb[] = "valentino";
	
	if(strcmp(array,arrayb) == 0){
		cout<<"is the same"<<endl;
	}
	else{ //osea distinto a 1
		cout<<"is not the same"<<endl;
		
	}
	
	//para ver cual es mayor alfabeticamente
	 char arrayc[] = "plane";
	 char arrayd[] = "boat";
	if(strcmp(array,arrayb) > 0){
		cout<<arrayc<<" is major than "<<arrayd<<endl;
	}
	else{
		cout<<arrayd<<" is major than "<<arrayc<<endl;
	}
	//funcion strncmp() permite comprobar un solo caso osea una sola letra
	cout<<"///////////////////////////////////////////////////////////////////////////////////////////////////"<<endl;
	char word1[] = "hola";
	char word2[] = "helado";
	if(strncmp(word1,word2,1)== 0){
		cout<<"the firts letter is equal";
	}
	else{
		
		cout<<"the first letter is not equal ";
		
	}
	getch();
	return 0;
}