#include<iostream>
#include<conio.h>
using namespace std;
int main(){
    int i,n1;
    do{
     cout<<"introduca un n: "<<endl; cin>>n1;
     if(n1 > 0){
        i += n1;   
           }
     
        }while((n1 < -30)&& (n1 > 20));
    cout<<"el resultado es: "<<i;
    
    
    getch();
    return 0;
    }
