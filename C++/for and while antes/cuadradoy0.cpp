#include<iostream>
#include<conio.h>
using namespace std;
int main(){
   double n,i= 0,r;
   do{
   cout<<"digite un numero"<<endl; cin>>n;
   if(n > 0){
      r = n*n;
      cout<<"el resultado es: "<<r;
      i++;
        }   
      
       }while(i<= 10);
   
   getch(); 
  return 0;  
}
