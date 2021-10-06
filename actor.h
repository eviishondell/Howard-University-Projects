#ifndef ACTOR_H
#define ACTOR_H
#include <iostream> 
#include <string>
using namespace std;


class Actor //label the class
{
  public: //can vary
  Actor();
  Actor(string name2 , float net2); //constructor
  void setName(string name1); //sets the variable
  void setNetworth(float net1); // sets the variable
  string getName(); //value returning
  float getNetworth(); //value returning
  
  
  private: //user cant change
  string name; //make name a string 
  float networth;//make networth a float
};
/*Create a header file called “Actor.h” with name and net 
worth variables, and function prototypes for a constructor 
and get/set functions for the name and net worth variables*/



