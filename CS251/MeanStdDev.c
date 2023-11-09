#include <stdio.h>
#include <math.h>

void main(){
	//Ask user and take input for numbers to average
	printf("Enter 10 numbers\n");

    //create variables to keep track
    double nums[10];
    double sum = 0;

    //Add up all the values we read in
    for(int i = 0; i < 10; i++){
        scanf("%lf", &nums[i]);
        sum += nums[i];
    }

    //Divide to find our mean
    double mean = sum/10;

    //Reset the sum for use in std.dev. and create variance array
    sum = 0;
    double variance[10];

    //Each data point minus the mean, then square it
    for(int i = 0; i < 10; i++){
        variance[i] = (nums[i] - mean)*(nums[i] - mean);
        sum += variance[i];
    }

    double stdDev = sqrt(sum/10);

    printf("Mean = %lf", mean);
    printf("Standard Deviation = %lf", stdDev);
}
