#include<iostream>

using namespace std;
int main() {
	char vec1[] = { 'a','b','c' };
	char vec2[] = { 'd','e','f' };
	char result[6];
	for (int i = 0; i <= 2; i++) {
		result[i] = vec1[i];
	}
	for (int i = 0; i <= 2; i++) {
		result[i + 3] = vec2[i];
	}
	for(int i = 0;i <= 6;i++){
		cout<<result[i]<<endl;
		
	}
}