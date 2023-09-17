#include<iostream>
using namespace std;
int main(){
	int matrix[100] [100],rows,columns;
	cout<<"type the number of  rows: "<<endl; cin>>rows;
	cout<<"type the number of  columns: "<<endl; cin>>columns;
	
	for(int i = 0;i < rows;i++){
		for(int j = 0;j < columns;j++){
			cout<<"type the number of : "<<i<<" "<<j<<" "; cin>>matrix[i][j];
		}

	}		
	for(int h = 0,j = 0,i = 0;h < rows;h++){
		cout<<matrix[i][j]<<endl;
		i += 1;
		j += 1;
		}
		
	return 0;
}