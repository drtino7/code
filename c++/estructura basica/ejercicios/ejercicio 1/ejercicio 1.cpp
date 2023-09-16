// ejercicio 1
#include<iostream>
#include<conio.h>

using namespace std;

struct corredor {
	char nombre[20];
	int edad;
	char sexo[20]; 
	char club[20];
}corredor1;

int main() {

	fflush(stdin);

	cout << "digite su nombre: ";
	cin.getline(corredor1.nombre,20,'\n');

	cout << "digite su edad: ";
	cin >> corredor1.edad;

	cout << "sexo: masculino o femenino ";
	cin.getline(corredor1.sexo, 20, '\n');

	cout << "digite su club: ";
	cin.getline(corredor1.club, 20, '\n');

	if (corredor1.edad <= 18) {
		char categoria[] = "junior";
	}

	if (corredor1.edad >18 && corredor1.edad <= 40) {
		char categoria[] = "veterano";
	}

	if (corredor1.edad > 40) {
		char categoria[20] = "veterano";
	}

	cout << corredor1.nombre;

	_getch();
	return 0;
}