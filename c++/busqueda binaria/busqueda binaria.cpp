// busqueda binaria
#include<iostream>
#include<conio.h>
using namespace std;
int main() {

	int numeros[] = { 1,2,3,4,5 };
	int sup, inf, mitad, dato;
	bool band = false;
	dato = 4;
	//algoritmo

	inf = 0;
	sup = 5;
		while (inf <= sup) {

			mitad = (inf + sup) / 2;

			if (numeros[mitad] == dato) {
				band = true;
				break;
			}
			if (numeros[mitad]> dato) {
				sup = mitad;
				mitad = (inf + sup) / 2;

			}
			if (numeros[mitad]< dato) {
				inf = mitad;
				mitad = (inf + sup) / 2;

		}
		}
	if (band == true) {
		cout << "encontrado";
	}
	else {
		cout << "no encontrado";
	}
	_getch();
	return 0;
}