#include <iostream>
#include <iomanip>
using namespace std;

void printMessage(float n1,float n2, float answerr, char oper) //doesnt return anything
{
  cout << n1 << oper << n2 << " = " << fixed << showpoint << setprecision(1) << answerr << endl; // print out equation
}

float calculate(float number1,float number2, char operation) //returns answer
{
  float count = 0;
  if (operation == '+') //add
  {
    count = number1+number2;
  }
  else if (operation == '-') //subtract
  {
    count = number1-number2;
  }
  else if (operation == '*') //multiply
  {
    count = number1*number2;
  }
  else if (operation == '/') //divide
  {
    count = number1/number2;
      
  }
  return count; //output
}
int main()
{
  bool keepGoing; //initialize everything
  char op;
  float num1,num2,answer;
  string decision;
  while(keepGoing){ //keep going makes the function run after final step
    
  
  cout << "Enter first number(0.0-999.99)" << endl; //prompt
  cin >> num1; //intake number
  cout << "Enter second number(0.0-999.99)" << endl;//prompt
  cin >> num2;//intake number
  cout << "Enter the operation(+,-,*,/)" << endl;//prompt
  cin >> op;//intake operation
  answer = calculate(num1,num2,op); //final answer
  printMessage(num1,num2,answer,op); //print equation
  cout << "Would you like to calculate more numbers?(yes/no)" << endl;//prompt
  cin >> decision; //yes or no
  if (decision == "yes")//yes makes it loop again
  {
    keepGoing = true;
  }
  else //no makes it stoo
  {
    keepGoing = false;
    cout << "Thanks for using the basic calculator" <<endl; //thank user
  }
}

}


