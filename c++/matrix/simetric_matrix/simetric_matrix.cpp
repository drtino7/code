#include<iostream>
using namespace std;
int main(){
	int matrix1[100][100],rows,columns,a = 0,b = 0;
	cout<<"type the number of  rows: "<<endl; cin>>rows;
	cout<<"type the number of  columns: "<<endl; cin>>columns;
	
	for(int i = 0;i < rows;i++){
		for(int j = 0;j < columns;j++){
			cout<<"type "<<i<<" "<<j<<": "; cin>>matrix1[i][j]; cout<<"\n";
		}
	}
	for(int i = 0;i < rows;i++){
		for(int j = 0;j < columns;j++){
			if(matrix1[i][j] == matrix1[j][i] && rows == columns){
				a = a + 1;
			}
			else{
				break;
			}

		}
	}
	if(a == rows * columns){
		cout<<"it's simetric"<<endl;
	}
	else{
		cout<<"it's not simetric"<<endl;
	}
	return 0;
}