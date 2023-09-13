#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int matriz1[100][100],filas,columnas,a = 0,b = 0;
	cout<<"digite el numero de filas: "<<endl; cin>>filas;
	cout<<"digite el numero de columnas: "<<endl; cin>>columnas;
	
	for(int i = 0;i < filas;i++){
		for(int j = 0;j < columnas;j++){
			cout<<"digite "<<i<<" "<<j<<": "; cin>>matriz1[i][j]; cout<<"\n";
		}
	}
	for(int i = 0;i < filas;i++){
		for(int j = 0;j < columnas;j++){
			if(matriz1[i][j] == matriz1[j][i] && filas == columnas){
				a = a + 1;
			}
			else{
				break;
			}

		}
	}
	if(a == filas * columnas){
		cout<<"es simetrica"<<endl;
	}
	else{
		cout<<"no es simetrica"<<endl;
	}
	getch();
	return 0;
}