#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;
int main(){
	
	char name[] = "tino";
	int len = strlen(name);
	reverse(name , name + len);
	
	cout<<name;
	return 0;
}