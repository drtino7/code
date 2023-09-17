// estructuras anidadas
#include<iostream>

using namespace std;

struct adress {
	char country[20];
	char street[20];
	int number;
};

struct empleado {
	char name[20];
	struct adress adress_employees;
	double salary;
}employees[2];


int main() {

	for (int i = 0; i < 2; i++) {
		fflush(stdin); //empty the buffer
		cout << "type the employer name";
		cin.getline(employees[i].name, 20, '\n');

		cout << '\n' << "type your country: ";
		cin.getline(employees[i].adress_employees.country, 20, '\n');
		cout << "'\n'type the name of the street: ";
		cin.getline(employees[i].adress_employees.street, 20, '\n');
		cout << "'\n'type the number of the house: ";
		cin >> employees[i].adress_employees.number;

		cout << "'\n'type the salari: ";
		cin >> employees[i].salary;
	}

	for (int i = 0; i < 2; i++){
		cout << "name: " << employees[i].name << endl;
	cout << "county: " << employees[i].adress_employees.country << endl;
}
	return 0;
}