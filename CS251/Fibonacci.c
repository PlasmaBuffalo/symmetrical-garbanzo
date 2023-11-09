#include <stdio.h>

void main(){
	//Ask user and take input for fNum (Fibonacci number)
	printf("Enter the number of the Fibonacci sequence you want\n");
	int fNum;
	scanf("%d", &fNum);

	//Variables to keep track of the numbers needed in the sequence
	int fm1 = 0;
	int fm2 = 1;
	int fm3 = fm1 + fm2; 
	int temp;

	//If input is 1 or 2, just print the first two numbers that we already know
	if(fNum == 1)
	printf("%d", fm1);
	else if(fNum == 2)
	printf("%d", fm2);
	//Otherwise, create a for-loop to calculate Fibonacci numbers until the input point is reached
	else{
		for(int a = 3; a < fNum; a++){
		temp = fm2;
		fm2 = fm3;
		fm1 = temp;
		fm3 = fm1+fm2;
		
	  }
   printf("%d", fm3);
	}
//Some of the first FS numbers for reference
//0, 1, 1, 2, 3, 5, 8, 13, 21, 34
	
}
