#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int matriz[100][100],filas,columnas;
	cout<<"\ndigite el numero de filas: "; cin>>filas;
	cout<<"\ndigite el numero de columnas: "; cin>>columnas;
	for(int i = 0;i < filas;i++){
		for(int j = 0;j < columnas;j++){
		cout<<"digite el numero de: "<<i<<" "<<j<<endl;
		cin>>matriz[i][j];
	}
	}
	for(int i = 0;i < filas;i++){
		for(int j = 0;j < columnas;j++){
		cout<<matriz[i][j]<<" ";	
		}
		cout<<endl;
	}
	
	getch();
	return 0;
}