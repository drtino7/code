#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int matriz[2][2] = {{1,2},{3,4}},copia[2][2];
	for(int i = 0; i < 2;i++){
		for(int j = 0; j < 2;j++){
		
		copia[i][j] = matriz[i][j];
}
	}
		for(int i = 0; i < 2;i++){
			for(int j = 0; j < 2;j++){
				cout<<copia[i][j]<<" ";
			}
		cout<<"\n";
	}
		
	
	
	getch();
	return 0;
}