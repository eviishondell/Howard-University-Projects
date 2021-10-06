#include <iostream>
using namespace std;

//Your heading function should ask the user for their name and print it

void heading_function(); //function prototype

//ur printMessage function should print the message to the user            
void printMessage(string, int); //function prototype

//Your getCredits function should determine how many more credits the user needs based on their major
//-Computer Engineering (82 credits) c
//-Electrical Engineering (80 credits) e
//-Computer Science(75 credits) s
//-Math(85 credits) m
int getCredits(int , char);  //function prototype         
            
            
            
int main()
{
  heading_function(); //call it
  char letter; //initialize
  int credits; //initialize
  string userMajor; //initialize
  int rCredits; //initialize
  cout << "Enter the letter your major: \n(C = Computer Engineering, E = Electrical Engineering , M = Math, S = Computer Science)" << endl; //prompt user
  cin >> letter; //take in the letter
  if(letter == 'C') // if it is C it is comp eng
  {
    userMajor = "Computer Engineering";
      
  }
  
  else if(letter == 'E')//if it is Eit is Elect eng
  {
    userMajor = "Electrical Engineering";
  }
  
  else if(letter == 'M') //if it is M it is Mechanical Engineering
  {
    userMajor = "Mechanical Engineering";
  }
  
   else if(letter == 'S') //if it is S it is CS
  {
    userMajor = "Computer Science";
  }
  
  cout << "How many credits have you completed?" << endl; //ask for completed credits
  cin >> credits; //intake
  rCredits = getCredits(credits , letter); //remaining credits = return statement from getcreds
  printMessage(userMajor, rCredits); //print out major and remaining
  
  
  
  return 0; //check
}


//Your getCredits function should determine how many more credits the user needs based on their major
//-Computer Engineering (82 credits) c
//-Electrical Engineering (80 credits) e
//-Computer Science(75 credits) s
//-Math(85 credits) m

int getCredits(int n , char l) { //2 parameters to intake
  
  if (l == 'C') //c means comp eng cred load subtracted from amt taken
  {
    return 82 - n ;
  }
  else if (l == 'E') //e means elect eng cred load subtracted from amt taken
  {
    return 80 - n ;
  }

   else if (l == 'S') //s means cscred load subtracted from amt taken
  {
    return 75 - n ;
  }
            
   else if (l == 'M') //m means mech eng cred load subtracted from amt taken
  {
    return 85 - n ;
    }
  }           
  
void printMessage(string userMajor, int rCredits) { //final print statement
   cout << "As a " << userMajor << " Major, you still need " << rCredits << " credits to graduate" << endl; 
}
            
void heading_function() { // takes in name and and says hello to user
  string name;
  cout << "What is your name?" << endl;
  getline(cin,name);
  cout << "Hello " << name << endl; 
}    
            
