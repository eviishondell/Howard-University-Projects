#include <iostream>
#include <string>
using namespace std;
int main()
{
    //bool keepGoing = true;   //not needed never asked user if they wanted to keep going
    int myNumber1 = 0; //initialize
    int myNumber2 = 0; //initialize
    int i=0; //loop over for i
    char op = ' '; //signs r characters
    //while(keepGoing)
    {
      cout << "Enter 2 numbers" << endl; //prompt
      cin >> myNumber1  >> myNumber2; //take numbers
      cout << "Enter an operation (/,%,*)" << endl; //prompt
      cin >> op; //take the sign
      if(op == '*') //multiply them
       {
         cout << myNumber1*myNumber2 << endl; //same
       }
      
       else if (op == '/' || '%') //use r to separate and divide and get remainder
       {
       cout << myNumber1/myNumber2 << " R " << myNumber1%myNumber2 << endl; //print
        }
      //do 3 times
      {
      cout << "Enter 2 numbers" << endl;
      cin >> myNumber1  >> myNumber2;
      cout << "Enter an operation (/,%,*)" << endl;
      cin >> op;
      if(op == '*')
       {
         cout << myNumber1*myNumber2 << endl;
       }
      
       else if (op == '/' || '%')
       {
       cout << myNumber1/myNumber2 << " R " << myNumber1%myNumber2 << endl;
        }
        
        {
      cout << "Enter 2 numbers" << endl;
      cin >> myNumber1  >> myNumber2;
      cout << "Enter an operation (/,%,*)" << endl;
      cin >> op;
      if(op == '*')
       {
         cout << myNumber1*myNumber2 << endl;
       }
      
       else if (op == '/' || '%')
       {
       cout << myNumber1/myNumber2 << " R " << myNumber1%myNumber2 << endl;
        }
          
          
    return 0;
        }
      }
}
}
