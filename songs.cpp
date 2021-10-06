#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std; 

int main()
{
  ifstream song_list;  //reads the file 
  song_list.open("file.txt"); // opens the file
  
  float listen_sum = 0; // sum of listens are initialized at 0
  int song_count = 0; //counts the amount of times the word "song" comes up
  float average = 0; //average is initialized
  string line; //song, artist name, listen
  string song_name , artist_name ; //declare variables
  int listen_number; // declare variable for amt of listens

  while (!song_list.eof()) //loop til the end of the file
  {
    getline(song_list,line); //getline gets everything after the space. it comes from my file name 
    if (line.substr(0,1) == "S") { //look at first word and first letter - checks for song
      getline(song_list,song_name); //makes it able to print the whole line including spaces

    }
    else if (line.substr(0,1) == "A") { //look at first word and first letter - checks for artist
      getline(song_list,artist_name); //makes it able to print the whole line including spaces
   
    }
    else if (line.substr(0,1) == "L") { //look at first word and first letter - checks for listen
      song_list >> listen_number; //makes it able to print the whole line including spaces
      
      listen_sum += listen_number; //listen number is added on to the sum until it reaches the end of the file - gives total
      song_count++; //increments by 1. so that we can get a denominator for the average
      cout << "Song Title: " << song_name << setw(28) << "Artist: " << artist_name << endl << "Listens: " << listen_number << endl << endl << endl; //prints out the the file info
    }
  }

  average = listen_sum / song_count; // average is sum total over amt of occurence
  cout << "Total Listens: " << listen_sum << endl; // prints out amt of listens
  cout << "Average Listens: " << setprecision(1) << fixed<< average; //prints out average ^^
  song_list.close(); //closes file
  return 0; //if it returns 0 it is running correctly with no errors
}

