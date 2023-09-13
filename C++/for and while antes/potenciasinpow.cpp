#include<iostream>
#include<conio.h>
using namespace std;
int main(){
    int x,y,r= 0;

    cout<<"in n"<<endl; cin>>x;
    cout<<"in n"<<endl; cin>>y;
    r = x;
    for(;y > 1;y--){
     r= x * r;                
               }
    cout<<"sl res es: "<<r;
    
    
    getch();
    return 0;
    }
