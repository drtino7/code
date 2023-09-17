//basic struct

#include<iostream>

using namespace std;
struct person {
	int age;
	char name[20];
}
person1 = { 15,"valentino" },
person2 = { 40,"juan" },
person3,person4
;

int main() {

	cout << "name 1:" << person1.name<<endl;
	cout << "age 1: " << person1.age<<endl;
	cout << "--------------------------"<<endl;
	cout << "name 2:" << person2.name << endl;
	cout << "age 2: " << person2.age << endl;
	cout << "----------------------" << endl;
	cout << "type your name: ";
	cin.getline(person3.name, 20, '\n');
	cout << "your name is: " << person3.name << endl;
	return 0;
}
