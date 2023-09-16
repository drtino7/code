//interseccion method
#include<iostream>
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
	cout<<"asendent order: ";
	for(i=0;i<5;i++){
		cout<<array[i];
	}
	cout<<'\n'<<"desendent order: ";
	for(i=4;i>=0;i--){
		cout<<array[i];
	}
	return 0;
}
