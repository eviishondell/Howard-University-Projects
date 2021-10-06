#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

float formula_(float x_f , float y_f)
{
  float answer; //float helps when returning decimal answer
  answer = (x_f+y_f)/3-(x_f-y_f)/5; //formula
  return answer; //return it

}

int main()
{
  ifstream reader; //initialize
  reader.open("file.txt");
  string calc1,calc2,x,equal1,y,equal2, newNum  ;
  float x1,y1,y2; //initialize
  float answer; //initialize
  while (!reader.eof()) //read to end of file
  {
    reader >> calc1 >> calc2; // reads header
    reader >> x >> equal1 >>  x1 >> y >> equal2 >> y2;   //reads te line after
    cout << calc1 << " " <<calc2 << " " << showpoint << fixed << setprecision(2) << formula_(x1,y2) << endl; //rounds
  }

  
