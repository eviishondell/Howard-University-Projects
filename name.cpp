#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
  ifstream reader; // declare a file object
  cout << "Please enter your full name: " << endl; //prompt user to enter full name
  string name; //input name
  getline(cin,name); // get string with spaces
  cout << "Your name is " << name << endl; // print out full statement
  return 0; //make sure program ran smoothly
    
}
