#include<iostream>
#include<conio.h>
using namespace std;
int main(){
 int numero,resultado = 1,finalresult = 0,i;
 cout<<"digite un numero: "<<endl; cin>>numero;
 i = 1;
 
 for(;i <= numero;i++){
 
 resultado *= i;
 finalresult += resultado;
} 
 cout<<"the result is: "<<finalresult<<endl;           
 getch();  
 return 0;   
}
