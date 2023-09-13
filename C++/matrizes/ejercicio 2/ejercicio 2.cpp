#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int matriz[100] [100],filas,columnas;
	cout<<"digite el numero de filas: "<<endl; cin>>filas;
	cout<<"digite el numero de columnas: "<<endl; cin>>columnas;
	
	for(int i = 0;i < filas;i++){
		for(int j = 0;j < columnas;j++){
			cout<<"digite el numero de: "<<i<<" "<<j<<" "; cin>>matriz[i][j];
		}

	}		
	for(int h = 0,j = 0,i = 0;h < filas;h++){
		cout<<matriz[i][j]<<endl;
		i += 1;
		j += 1;
		}
			getch();
	return 0;
}