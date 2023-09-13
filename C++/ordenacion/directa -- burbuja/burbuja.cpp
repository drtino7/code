//metodo burbuja
#include<iostream>
#include<conio.h>
 using namespace std; 
 int main(){

	int array[] = {4,1,2,3,5};
	int i,j,aux;
	
	for(i=0;i<5;i++){
		for(j=0;j<5;j++){
			if(array[j] > array[j + 1]){
				aux = array[j];
				array[j] = array[j+1];
				array[j+1] = aux;
			}
		}
	}
cout<<"orden acendente: ";
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