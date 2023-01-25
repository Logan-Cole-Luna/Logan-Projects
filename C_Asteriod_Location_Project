/*This program asks the user for their credentials, and after verifying that they 
are correct with
fileIO it proceeds to create a random array of asteroids, calculate their distance 
from the user(0,0),
and print the X, Y, & Z points in an asteroid file and these along with the 
distance in a distance file.
After doing so the program warns the user of asteroid proximity, and graphs the 
distance of each asteroid*/
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>
#define SIZE_OF_NAME 6
#define USER_NUMBER 6
#define ATTEMPTS 2
#define ASTROID_NUMBER 10
#define ASTROID_SPEED 30
#define COORDINATE_MIN 10
#define COORDINATE_MAX 1000
#define NUMBER_OF_NAMES 6
#define WARNING_DISTANCE 750
#define DISTANCE_INCREMENT 20
//prototypes
bool validateFunct(char nameChoiceUser[SIZE_OF_NAME], char 
idChoiceUser[SIZE_OF_NAME]);
int asteroidDistance(int x, int y, int z);
int asteroidLocation();
int randFunct(int rangeMin, int rangeMax);
float asteroidGraph(float dist);
//Structure for identifying User
struct user
{
  char fileName[SIZE_OF_NAME];
  char fileID[SIZE_OF_NAME];
};
//Structure for asteroid characteristics
struct asteroid
{
  char ch[SIZE_OF_NAME];
  int cordX;
  int cordY;
  int cordZ;
  float distance;
};
int main(void)
{
  //declares and initializes variables
  int index_counter = 0;
  bool validation = false;
  //declares character arrays
  char choiceNameByUser[SIZE_OF_NAME], choiceIdByUser[SIZE_OF_NAME];
  //declaring array of structure with 10 elements
  struct user record[10];
  //Making random values for random function
  srand(time(NULL));
  printf("Logan Lambeth's Program\n\n");
  //asks user for name and id number
  printf("Enter your name\n");
  scanf("%s", &choiceNameByUser);
  printf("Enter your ID number\n");
  scanf("%s", &choiceIdByUser);
  // Validating name & ID input
  if ((validateFunct(choiceNameByUser, choiceIdByUser)) == true)
  {
    //If inputs are correct
    printf("\nWelcome %s\n", choiceNameByUser);
    printf("========================\n");
    //Function to determine asteroid location
    asteroidLocation();
    printf("========================\n");
  }
  else
  {
    printf("\nNo attempts remaining, terminating program.\n");
    return 0;
  }
  return 0;
}
// Random integer function
int randFunct(int rangeMax, int rangeMin)
{
  return rangeMin + rand() % (rangeMax+1 - rangeMin);
}
// Validating user input function
bool validateFunct(char nameChoiceUser[SIZE_OF_NAME], char 
idChoiceUser[SIZE_OF_NAME])
{
  int stringNameCompare = 1, stringIDCompare = 1, i = 0, index_counter = 0;
  bool correctInputs = false;
  //declaring array of structure with 10 elements
  struct user record[USER_NUMBER];
  //Opening file
  FILE *FpointinUserID = fopen("ident.txt","r");
  //Checks if files exist for ID
  if (FpointinUserID == NULL)
  {
    printf ("File is not found");
  }
  //Primary loop for checking user credentials
  do
  {
    //Scanning each file name & ID
    while (fscanf(FpointinUserID,"%s %s",record[index_counter].fileName, 
record[index_counter].fileID)==2)
    {
      index_counter++;
    }
    //Loop comparing credentials and input
    for(index_counter = 0; index_counter < ASTROID_NUMBER; index_counter++)
    {
      stringNameCompare = strcmp(nameChoiceUser, record[index_counter].fileName);
      stringIDCompare = strcmp(idChoiceUser, record[index_counter].fileID);
      //If user input was correct
      if ((stringNameCompare == 0) && (stringIDCompare == 0))
      {
        printf("\nCorrect!\n");
        correctInputs = true;
      }
    }
    //Checking # of attempts left
    if((i != ATTEMPTS+1) && (correctInputs != true))
    {
      //Informing user about incorrect input
      printf("\n%s is an incorrect name or %s is an incorrect ID", nameChoiceUser, 
idChoiceUser);
      printf("\nAttempts Remaining: %d\n", ATTEMPTS-i);
      //Indexing attempt number
      i++;
      //Allowing user to input credentials again
      printf("Please enter your name again\n");
      scanf("%s", nameChoiceUser);
      printf("Please enter your ID again\n");
      scanf("%s", idChoiceUser);
    }
  }while ((i != ATTEMPTS+1) && (correctInputs != true)); //Doing loop while 
//credentials are not correct
  //closing file
  fclose(FpointinUserID);
  return correctInputs;
}
int asteroidLocation()
{
  //Initializations
  int j = 0, k = 0, f = 0, h = 0;
  char character='A';
  struct asteroid location[ASTROID_NUMBER];
  //Opening files with W+ to write and read from them
  FILE *FpointinAsteroids = fopen("asteroids.txt","w+");
  FILE *FpointinDistance = fopen("distance.txt","w+");
  //Random generator of asteroid coordinates
  for (k = 0; k < ASTROID_NUMBER; k++)
  {
    //Generates numbers from 10 to 1000 in 10 element array
    location[k].cordX = randFunct(COORDINATE_MAX, COORDINATE_MIN);
    location[k].cordY = randFunct(COORDINATE_MAX, COORDINATE_MIN);
    location[k].cordZ = randFunct(COORDINATE_MAX, COORDINATE_MIN);
    //Calling distance calculation function
    location[k].distance = asteroidDistance(location[k].cordX, location[k].cordY, 
location[k].cordZ);
    //Printing results in console
    printf("\n%c: X: %d, Y: %d, Z:%d\n",character + k, location[k].cordX, 
location[k].cordY, location[k].cordZ, location[k].distance);
    //Printing results in Asteroids file
    fprintf(FpointinAsteroids, "%c %d %d %d\n", character + k, location[k].cordX, 
location[k].cordY, location[k].cordZ);
    //Printing results in Distance file
    fprintf(FpointinDistance, "%c\t %d\t %d\t %d\t %.2lf\n", character + k, 
location[k].cordX, location[k].cordY, location[k].cordZ, location[k].distance);
  }
  printf("========================\n");
  //For loop checking distance of each asteroid distance from ship & informing if close
  for (f = 0; f < ASTROID_NUMBER; f++)
  {
    if (location[f].distance < WARNING_DISTANCE)
    {
    printf("\nWarning! Asteroid %c is %.2lf km away!\nTime to impact: %.2lf Second\
n", character+f, location[f].distance, location[f].distance / ASTROID_SPEED);
    }
  }
  //Loop calling asteroidGraph function and displaying graph
  printf("\nAsteroid Location Table\n* = 20 km\n");
    printf("========================\n");
  for(h = 0; h < ASTROID_NUMBER; h++)
  {
    //printf("%.2lf\t", location[i].distance);
    printf("%c: ", character+h);
    asteroidGraph(location[h].distance);
    printf("\n");
  }
  //Final bottom for graph
  printf("-------|------|------|------|------|------|------|------|------|------|------|------|\n");
  printf("   0     140    280    420    560    700    1120   1260   1400   1540   1680   1820\n");
  //Closing files
  fclose(FpointinAsteroids);
  fclose(FpointinDistance);
}

//Function for calculating distance using formula
int asteroidDistance(int x, int y, int z)
{
  float distance = 0;
  distance = pow(pow(x,2)+pow(y,2)+pow(z,2),0.5);
  return distance;
}
//Function for graphing distance of asteroids
float asteroidGraph(float distanceAsteroid)
{
  int value = 0;
  while (value < distanceAsteroid)
  {
    printf("*");
    //Printing a star for each distance of 20
    value = value + DISTANCE_INCREMENT;
  }
}
