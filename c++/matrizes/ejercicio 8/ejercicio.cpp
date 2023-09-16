#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int a[3][3] = {{1,2,1},{2,1,1},{2,1,2}};
	int b[3][3] = {{3,2,1},{2,3,1},{1,1,3}};
	int c[3][3];
	for(int i = 0;i<3;i++){
		for(int j = 0;j<3;j++){
		c[i][j] = 0;
			for(int k = 0;k<3;k++){
				c[i][j] += a[i][k] * b[k][j];
			}	
		}
	}
for(int i = 0;i < 3;i++){
	for(int j = 0;j<3;j++){
		cout<<c[i][j]<<" ";
	}
	cout<<"\n";
}	
getch();	
return 0;
}