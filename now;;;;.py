include<iostream.h>
include<conio.h>

void main()
{
     clrscr();// clear the screen
    
    //Declare an array of integers with a size of 5 int numbers[];

    // Prompt the user to enter 5 integers and store then in the array
    cout <<"Enter 5 integers:"<<endl;
    for (int i = 0;i<5;++i){cout<<"Enter integers:"<<i+1<<":";}

    //Display the elements of the array cout <<"The elements you entered are:";
    for(int i=0;++i){cout<<numbers[i]<<"";}
cout<<endl
getch();//wait for a key press 
}