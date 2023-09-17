#include<iostream>
#include<conio.h>
using namespace std;
int main() {
	int vector[5], sumat;
	for (int i = 0; i <= 4; i++) {
		cout << "digite un numero: " << endl; cin >> vector[i];
		sumat += vector[i];
	}

	for (int i = 0; i <= 4; i++) {
		if (vector[i] == sumat - vector[i]){
			cout << vector[i] << " es la suma de todos los numbers" << endl;}

	}


	getch();
	return 0;
}