#include<conio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main(){
	
	char name[20];
	int lenght;
	int a  = 0;
	cout<<"tipe your name: ";
	cin.getline(name,20,'\n');
	strlwr(name);
	for(int i = 0;i < strlen(name);i++){
switch(name[i]){
	case 'a': a++; break;
	case 'e': a++; break;
	case 'i': a++; break;
	case 'o': a++; break;
	case 'u': a++;break;
}	
	}
cout<<a<<endl;
			
	getch();
	return 0;
}