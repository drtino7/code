#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include<time.h>
using namespace std;
int main(){
int number,random,attemps = 0;
srand(time(NULL));//hace que cambie el rand()
random =  1 + rand()%(100);//genera un numero al azar entre 1 y 100
do{
cout<<"type a number between 1 and 100: "<<endl; cin>>number;
attemps++;
if(number < random){
	cout<<"the number is minor than the random number "<<endl;
}
if(number > random){
	cout<<"the number is higher than the random number "<<endl;
}

}while(number != random);
cout<<"you are right!! the random number is: "<<random<<endl;
cout<<"you did it in this number of attemps: "<<attemps<<endl;
getch();
return 0;
}