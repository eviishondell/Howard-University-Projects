#include <iostream>
#include "actor.h"

Actor::Actor() //name of class :: name of the constructor member function
  {
    name = "";
    networth = 0;
  }
  Actor::Actor(string name2 , float net2) //class::object
  {
    name = name2; //assign namet to name
    networth = net2; //assign net2 to networth
  }
  void Actor::setName(string name1) //set name member function 
  {
    name = name1; // assigning name the value of the parameter being passed
  }
  void Actor::setNetworth(float net1) //set networth member function 
  {
    networth = net1; // assigning networth the value of the parameter being passed
  }
  string Actor::getName() //set name member function 
  {
    return name; //returning the value of name
  }
  float Actor::getNetworth() //set networth member function 
  {
    return networth; //returning networth value
  }

