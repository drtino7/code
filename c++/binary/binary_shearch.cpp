#include<iostream>

using namespace std;

int main() {

	int numbers[] = { 1,2,3,4,5 };
	int sup, inf, half, data;
	bool band = false;
	data = 4;
	//algorithm

	inf = 0;
	sup = 5;
		while (inf <= sup) {

			half = (inf + sup) / 2;

			if (numbers[half] == data) {
				band = true;
				break;
			}
			if (numbers[half]> data) {
				sup = half;
				half = (inf + sup) / 2;

			}
			if (numbers[half]< data) {
				inf = half;
				half = (inf + sup) / 2;

		}
		}
	if (band == true) {
		cout << "found";
	}
	else {
		cout << "not found";
	}
	return 0;
}