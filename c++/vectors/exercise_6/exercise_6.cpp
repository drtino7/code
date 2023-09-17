#include<iostream>

using namespace std;
int main() {
	int vector[5], additiont;
	for (int i = 0; i <= 4; i++) {
		cout << "type a number: " << endl; cin >> vector[i];
		additiont += vector[i];
	}

	for (int i = 0; i <= 4; i++) {
		if (vector[i] == additiont - vector[i]){
			cout << vector[i] << " it's the addition of all the numbers" << endl;}

	}


	return 0;
}