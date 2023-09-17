#include<iostream>
using namespace std;
int main(){
	
	int matrix[3][3],coptras[3][3];
	
	for(int i = 0;i < 3;i++){
		for(int j = 0;j < 3;j++){
			cout<<"type "<<i<<" "<<j<<": "<<endl; cin>>matrix[i][j];
		}
	}
	
	for(int i = 0;i < 3;i++){
		for(int j = 0;j < 3;j++){
			coptras[j][i] = matrix [i][j];
		}
	}	
	for(int i = 0;i < 3;i++){
		for(int j = 0;j < 3;j++){
			cout<<coptras[i][j]<<" ";
		}
		cout<<endl;
	}

	return 0;
}