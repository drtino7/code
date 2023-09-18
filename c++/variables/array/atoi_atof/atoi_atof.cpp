//atoi atof
#include<iostream>
#include<stdlib.h>

using namespace std;
int main(){
	
	char array[] = "123";
	int number;
	 number = atoi(array);
	 cout<<number<<endl;
	
	char array2[] = "123.77";
	float number2;
	 number2 = atof(array2);
	 cout<<number2<<endl;	 
	 
	
	return 0;
}
