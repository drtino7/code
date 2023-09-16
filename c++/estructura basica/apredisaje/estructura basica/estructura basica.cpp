// estructura basica 

#include<iostream>
#include<conio.h>

using namespace std;
struct persona {
	int age;
	char name[20];
}
persona1 = { 15,"valentino" },
persona2 = { 40,"juan" },
persona3,persona4
;

int main() {

	cout << "nombre 1:" << persona1.name<<endl;
	cout << "edad 1: " << persona1.age<<endl;
	cout << "--------------------------"<<endl;
	cout << "nombre 2:" << persona2.name << endl;
	cout << "edad 2: " << persona2.age << endl;
	cout << "----------------------" << endl;
	cout << "type your name: ";
	cin.getline(persona3.name, 20, '\n');
	cout << "your name is: " << persona3.name << endl;
	_getch();
	return 0;
}
