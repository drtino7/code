#include<iostream>
#include<stdlib.h>  //new and delete

using namespace std;

int nGrades, *grades;

void asknotes();
void showGrades();



int main(){

asknotes();
showGrades();


delete[] grades;


return 0;
}


void asknotes(){
cout<<"type your number of grades: ";cin>>nGrades;

grades = new int[nGrades];

for(int i = 0; i < nGrades ;i++){
cout<<"type your grade: "; cin>>grades[i];
}
}

void showGrades(){
for(int i = 0 ; i < nGrades; i++){
cout<<grades[i]<<endl;

}




}
