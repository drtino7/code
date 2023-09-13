#include<iostream>
#include<stdlib.h>
using namespace std;
int main(){
  int resultado,n;
  cout<<"digite un numero: "<<endl;
  cin>>n;
  for(int n2 = 1; n2 <= 10; n2++){
          resultado = n * n2;
          cout<<"el resultado es: " <<resultado<<endl;
}
system("pause");
  return 0;
}
