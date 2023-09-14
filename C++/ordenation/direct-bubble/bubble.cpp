//metodo bubble
#include<iostream>
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
cout<<"asendent order: ";
for(i=0;i<5;i++){
	cout<<array[i];
}
cout<<'\n'<<"decendent order: ";
for(i=4;i>=0;i--){
	cout<<array[i];
}
 	return 0;
 }
