#include<iostream>
#include<conio.h>
#include<time.h>
#include<stdlib.h>
using namespace std;
int main(){
	int matriz[100][100],filas,columnas,copia[100][100];
	srand(time(NULL));
	cout<<"digite el numero de filas: "<<endl; cin>>filas;
	cout<<"digite el numero de columnas: "<<endl; cin>>columnas;
	
	for(int i = 0;i < filas;i++){
		for(int j = 0; j < columnas;j++){
			matriz[i][j] = 1 + rand()%(10000);
	}
}
for(int i = 0;i < filas;i++){
	for(int j = 0; j < columnas;j++){
	copia[i][j] = matriz[i][j];
		
	}
}

for(int i = 0;i < filas;i++){
	for(int j = 0; j < columnas;j++){
	cout<<copia[i][j]<<" ";
}
cout<<endl;
	}


	getch();
	return 0;
}