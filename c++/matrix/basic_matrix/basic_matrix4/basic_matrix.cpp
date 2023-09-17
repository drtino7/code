#include<iostream>
#include<time.h>
#include<stdlib.h>
using namespace std;
int main(){
	int matrix[100][100],rows,columns,copy[100][100];
	srand(time(NULL));
	cout<<"type the number of  rows: "<<endl; cin>>rows;
	cout<<"type the number of  columns: "<<endl; cin>>columns;
	
	for(int i = 0;i < rows;i++){
		for(int j = 0; j < columns;j++){
			matrix[i][j] = 1 + rand()%(10000);
	}
}
for(int i = 0;i < rows;i++){
	for(int j = 0; j < columns;j++){
	copy[i][j] = matrix[i][j];
		
	}
}

for(int i = 0;i < rows;i++){
	for(int j = 0; j < columns;j++){
	cout<<copy[i][j]<<" ";
}
cout<<endl;
	}


	return 0;
}