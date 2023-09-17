#include<iostream>
using namespace std;
int main(){
	int matrix[100][100],rows,columns;
	cout<<"\ntype the number of rows: "; cin>>rows;
	cout<<"\ntype the number of columns: "; cin>>columns;
	for(int i = 0;i < rows;i++){
		for(int j = 0;j < columns;j++){
		cout<<"type the number of : "<<i<<" "<<j<<endl;
		cin>>matrix[i][j];
	}
	}
	for(int i = 0;i < rows;i++){
		for(int j = 0;j < columns;j++){
		cout<<matrix[i][j]<<" ";	
		}
		cout<<endl;
	}
	
	return 0;
}