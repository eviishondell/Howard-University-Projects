#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;

/*read data from the file
 * save data to arrays
 * calculate sum and length of the arrays
 * calculate average
 * get final exam grade from user
 * calculate current grade 
 * print it out
 * */

float calculate(int length, float sum) //float returning function to calculate the average
{
  float average;//declare average
  average = (sum/(length*100))*100; // formula
  return average;// return the float

}
int main()
{
  string assessment; //declare assessment
  float current_grade;//declare currrent grade
  float labs[10]; //lab array
  float quizzes[10];//quiz array
  float assignments[10];//assignments array
  float midterm_exam,final_exam,p_exam,qsum = 0,asum = 0,lsum = 0; //qsum,asum,lsum counters and other variables are declared
  int l = 0,q = 0,a = 0; // index starts at 0 for looping through arrays

  ifstream reader; // declare reader
  reader.open("file.txt"); //open file.txt
  while(!reader.eof()){ //while not at end of file
   int grade = 0;  //grade is 0 until assigned
    reader >> assessment; //read as letter
    reader >> grade; //read as grade
    if (assessment == "L" || assessment == "P") //if l or p
    {
      labs[l] = grade; //in labs array the value at index l will be assigned the value of grade
      lsum += grade; //adds current value of lsum to grade
      l++; //increments
      //python = labs.append(grade)
    }
    else if (assessment == "Q") //if q
    {
      quizzes[q] = grade; //in quizzes array the value at index q will be assigned the value of grade
      qsum += grade;//adds current value of qsum to grade
      q++; //increment 
    }  
    else if (assessment == "A") //if a
    {
      assignments[a] = grade; //in assignment array the value at index a will be assigned the value of grade
      asum += grade;//adds current value of asum to grade
      a++;//increment
    }
    
    else if (assessment == "M") //if m
    {
      midterm_exam = grade; //assign midterm exam to grade
    }
  }
 
  cout << "Enter a grade for the final" << endl; //prompt user
  cin >> final_exam; //take in inout
  cout << "Labs: " << calculate(l+1,lsum) << endl; //display lab average
  cout << "Quizzes: " << calculate(q+1,qsum) << endl;//display quiz average
  cout << "Assignments: " << calculate(a+1,asum) << endl; //display assignment average
  cout << "Midterm Exam: " << midterm_exam << endl; //display midterm grade
  cout << "Final Exam: " << final_exam << endl; //display final grade
  current_grade = (calculate(l+1,lsum) * .1) + (calculate(q+1,qsum) * .05) + 
    (calculate(a+1,asum) *.1)+(midterm_exam * .35)+(final_exam * .4);
  //+<attendance_perecent> current grade calculation
  cout << "Current: " << current_grade << endl; //print current grade
  }

