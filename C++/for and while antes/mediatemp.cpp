#include<iostream>
#include<conio.h>
using namespace std;
int main(){
    float x,y,mayor = -50,menor = 100,media,total;
    for(x = 0;y < 24; y+= 4){
       cout<<"digite la temperatura: "<<endl; cin>>x;
       if(x > mayor){
           mayor = x;
        
            }
       if(x < menor){
            menor = x;
            }    
     media = (menor + mayor)/ 2;
     total = x + total;
     
          }
     
     cout<<"la media entre la temp > y la < es: "<<media<<endl;
     cout<<"la media del dia es: "<<total / 6<<endl;
   getch(); 
   return 0; 
    }
