#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	
	int matriz[3][3],coptras[3][3];
	
	for(int i = 0;i < 3;i++){
		for(int j = 0;j < 3;j++){
			cout<<"digite "<<i<<" "<<j<<": "<<endl; cin>>matriz[i][j];
		}
	}
	
	for(int i = 0;i < 3;i++){
		for(int j = 0;j < 3;j++){
			coptras[j][i] = matriz [i][j];
		}
	}	
	for(int i = 0;i < 3;i++){
		for(int j = 0;j < 3;j++){
			cout<<coptras[i][j]<<" ";
		}
		cout<<endl;
	}

	getch();
	return 0;
}