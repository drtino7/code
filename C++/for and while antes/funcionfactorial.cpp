#include<iostream>
#include<conio.h>
using namespace std;
int main(){ 
   int n,r= 1,i = 0,j;
   cout<<"digite un numero a factorizar"<<endl; cin>>n;

  for(int ii = n;ii > 1; ii-- ){
  
   for(;n > 1;n--){
   i++;
   r = (r * i)+ r;     
    
         }
    j = r + r;
    }
   cout<<"el resultado es: "<<j<<endl;
   
   
    
    getch();
    return 0;
    }
