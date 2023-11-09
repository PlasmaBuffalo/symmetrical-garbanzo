#include <stdio.h>

void main()
{
    //Ask user and take input for numbers to average
    printf("Average of Nums:");

    //Establish variables to keep track
    double sum = 0;
    int count = 0;
    int input;

    //Loop through file and read in each number
    while (input > 0)
    {
        scanf("%d", &input);
        sum += input;
        count++;
    }
    double final = sum / count;

    printf("%ld", final);
}
