//Gianni Russell
//November 28, 2023

#include <iostream>
using namespace std;
int main() {
    int numYears;
    cout << "Enter the number of years: ";
    cin >> numYears;
    double p = 325.70; 
    double B = 12.4/1000;
    double D = 8.4/1000;

    for(int i = 2017; i <2017+numYears; i++) {
        cout << "Year\t" << i << "\t"<< p << endl;
        p = p + B*p - D*p;
    }
}