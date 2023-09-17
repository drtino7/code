#include<iostream>
using namespace std;
int main(){
	int list[100],number,higher_number = 0;
	cout<<"type the number of elements that yopu want in the list: "<<endl; cin>>number;
	for(int i = 0;i < number;i++){
		cout<<"type the number of the vector: "<<endl;
		cin>>list[i];
	}
	for(int i = 0;i < number;i++){
		if(list[i]>higher_number) {
			higher_number = list[i];
		}
		
}
cout<<higher_number<<endl;	

return 0;
}