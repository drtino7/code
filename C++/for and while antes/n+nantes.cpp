#include<iostream>
#include<conio.h>
using namespace std;
int main(){
   int n,n1 = 1,i= 0;
   cout<<"digite un numero: "<<endl; cin>>n;
   n = n*2;
   for(;n >= n1;){
       n1 = n1 + 2;
        i= i + n1; 
          }
    cout<<"el resultado es: "<<i - 1;
   getch();
   return 0; 
   
}
