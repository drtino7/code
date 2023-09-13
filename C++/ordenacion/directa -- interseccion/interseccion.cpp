//metodo de interseccion
#include<iostream>
#include<conio.h>
using namespace std;
int main(){

	int array[] = {4,2,3,1,5};
	int i,pos,aux;

	for(i=0;i<5;i++){
		pos = i;
		aux = array[i];
			while((pos>0)and(array[pos-1]>aux)){
			array[pos] = array[pos-1];
			pos--;
			}
		array[pos] = aux;
	}
	cout<<"orden asendente: ";
	for(i=0;i<5;i++){
		cout<<array[i];
	}
	cout<<'\n'<<"orden desendente: ";
	for(i=4;i>=0;i--){
		cout<<array[i];
	}
	getch();
	return 0;
}