#include<iostream>
#include<conio.h>
#include<cmath>
using namespace std;
int main(){
   double n,i,r,var;
   cout<<"digite un numero: "<<endl; cin>>n;
   
   for(i = 1;i <= 10; i++){
         r = pow(n,i);
         var = var + r;
         cout<<"el resultado es: "<<var<<endl;
         }
   
  getch(); 
  return 0;  
}
