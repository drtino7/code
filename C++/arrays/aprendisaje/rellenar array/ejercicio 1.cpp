#include<iostream>
#include<string.h>
using namespace std;
int main(){
	//formas de almazenar una cadena
	
	
	//forma numero 1
	char nombre[] = "Valentino";
	char nombre2[] = {'V','a','l','e','n','t','i','n','o'};
	cout<<nombre<<"    forma uno "<<endl;
	cout<<nombre2<<"   forma 2 "<<endl;
	
	//forma 2 (al ver un espacio la acadena deja de rellenarce)
	cout<<"digite su nombre: ";
	cin>>nombre;
	cout<<nombre<<endl;
	
	//froma 3(no le importa la cantidad de espacios que contenga un array)
	char nombrea[5];
	cout<<"digite tu nombre: ";
	gets(nombrea);
	cout<<nombrea<<endl;
	
	//forma 3(forma correcta); consta de 3 parametros (nombre array)(cantidad de espacios)(cunado termina)
	char nombreb[5];
	cout<<"digite tu nombre: ";
	cin.getline(nombreb,5,'\n');
	cout<<nombreb;
	
	
	return 0;
}
