#include<iostream>
#include<string.h>

using namespace std;
int main(){
	char cat1[] = "hi";
	char cat2[] = " hi again";
	char cat3[20];
	
	strcpy(cat3,cat1);
	cout<<cat3<<endl;
	strcat(cat3,cat2);
	cout<<cat3<<endl;	
	
	 
	return 0;
}
