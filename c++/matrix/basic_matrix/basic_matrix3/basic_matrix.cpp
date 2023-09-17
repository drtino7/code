#include<iostream>
using namespace std;
int main(){
	int matrix[2][2] = {{1,2},{3,4}},copy[2][2];
	for(int i = 0; i < 2;i++){
		for(int j = 0; j < 2;j++){
		
		copy[i][j] = matrix[i][j];
}
	}
		for(int i = 0; i < 2;i++){
			for(int j = 0; j < 2;j++){
				cout<<copy[i][j]<<" ";
			}
		cout<<"\n";
	}
		
	
	

	return 0;
}