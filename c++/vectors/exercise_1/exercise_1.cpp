#include<iostream>

using namespace std;

int main(){
	
	int numbers[] = {1, 2, 3, 4, 5};
	int addition;
	for(int i = 0; i < 5; i++){
	addition += numbers[i];
}
cout<<addition;
	return 0;
}