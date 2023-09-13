#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	float prueba1,prueba2,prueba3,aprove_all_exams = 0,aprove_atleast_one_exam = 0,aprove_last_exam = 0;
	for(int i = 1;i <= 5;i++){
	cout<<"the note of the student number "<<i<<endl;
	cout<<"cual fue la nota de la primera prueba: "<<endl; cin>>prueba1;
	cout<<"cual fue la nota de la segunda prueba: "<<endl; cin>>prueba2;
	cout<<"cual fue la nota de la tercera prueba: "<<endl; cin>>prueba3;
	
		//start with aprove_atleast_one_exam
	if(prueba1 > 6){
	aprove_atleast_one_exam++;
	}
	if((prueba2 > 6)&&(prueba1 < 6)) {
	aprove_atleast_one_exam++;
	}
	if((prueba3 > 6)&&(prueba1 < 6)&&(prueba2 < 6)){
		aprove_atleast_one_exam++;
	}
	//end with aprove_atleast_one_exam
	//start with aprove_last_exam
	if(prueba3 > 6){
		aprove_last_exam++;
	}
	//end with aprove_last_exam
	//start with aprove_all_exams
		if((prueba3 > 6)&&(prueba1 > 6)&&(prueba2 > 6)){
		aprove_all_exams++;
		}
	}
	cout<<"the number of students who aprove at least one exam: "<<aprove_atleast_one_exam<<endl;
	cout<<"the number of student who aprove the last exam: "<<aprove_last_exam<<endl;
	cout<<"the number of students who aprove all the exams: "<<aprove_all_exams<<endl;
	
	getch();
	return 0;
}