#include <iostream>
using namespace std;

int main()
{
  int number = 0;
  int sum = 0;
  cout << "Enter a number(0-9)" << endl;
  cin >> number;
  sum += number;
  cout << "Enter a number(0-9)" << endl;
  cin >> number;
  sum += number;
  cout << "Enter a number(0-9)" << endl;
  cin >> number;
  sum += number;
  cout << sum;
  return 0;
}
