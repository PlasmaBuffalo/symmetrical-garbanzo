#include <math.h>
#include <stdio.h>
#include <stdlib.h>

//Main method
void main(int argc, char** argv)
{
    //declare variables
    int size;
    double* data;

    //take in size of array
    printf("Enter size of array: ");
    scanf("%d", &size);

    //use malloc to determine size of array
    data = (double*) malloc(size * sizeof(int));

    printf("Enter 10 elements: ");
    for (int i = 0; i < 10; ++i)
        scanf("%f", &data[i]);
    printf("\nMean = %lf", mean(data, size));
    printf("\nStandard Deviation = %lf", sd(data, size));

    free(data);
}

double mean(double data[], int size)
{
    double sum = 0.0;
    int i;
    for (i = 0; i < size; ++i)
    {
        sum += data[i];
    }
    double avg = sum / size;
    return avg;
}

double sd(double data[], int size)
{
    double sum = 0.0, avg, mc = 0.0;
    int i;
    for (i = 0; i < size; ++i)
    {
        sum += data[i];
    }
    avg = sum / size;
    for (i = 0; i < size; ++i)
    {
        mc += pow(data[i] - avg, 2);
    }
    return sqrt(mc / size);
}