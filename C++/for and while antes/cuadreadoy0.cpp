#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;
int main(){
   int n,i = 0,resultado = 0;
   do{
    cout<<"digite un numero"<<endl; cin>>n;
    if(n > 0){
      resultado= pow(n,2); 
      cout<<"el resultado es: "<<resultado<<endl;  
       i++;
         }
   else{
   cout<<"el numero no es mayor a 0"<<endl;
        }
  } while(n <= 10);
    
    
  getch();  
  return 0; 
}
