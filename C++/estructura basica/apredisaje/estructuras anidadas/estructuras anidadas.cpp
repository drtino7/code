// estructuras anidadas
#include<iostream>
#include<conio.h>

using namespace std;

struct adress {
	char country[20];
	char street[20];
	int number;
};

struct empleado {
	char name[20];
	struct adress adress_employer;
	double salario;
}empleados[2];


int main() {

	for (int i = 0; i < 2; i++) {
		fflush(stdin); //vacia el buffer
		cout << "type the employer name";
		cin.getline(empleados[i].name, 20, '\n');

		cout << '\n' << "type your country: ";
		cin.getline(empleados[i].adress_employer.country, 20, '\n');
		cout << "'\n'type the name of the street: ";
		cin.getline(empleados[i].adress_employer.street, 20, '\n');
		cout << "'\n'type the number of the house: ";
		cin >> empleados[i].adress_employer.number;

		cout << "'\n'type the salari: ";
		cin >> empleados[i].salario;
	}

	for (int i = 0; i < 2; i++){
		cout << "name: " << empleados[i].name << endl;
	cout << "county: " << empleados[i].adress_employer.country << endl;
}
	_getch();
	return 0;
}