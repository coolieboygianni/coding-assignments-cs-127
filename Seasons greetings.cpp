//Gianni Russell
//November 28, 2023

#include <iostream>
using namespace std;

int main(){
    int month;
    cout << "Enter month as a number: ";
    cin >> month;
    if (month < 3 || month > 11) {
    cout << "Happy Winter";
    }
    if (month >= 3 && month < 7) {
    cout << "Happy Spring";
    } 
    if (month >= 7 && month < 9) {
    cout << "Happy Summer";
    } else {
    cout << "Happy fall";
    };
}