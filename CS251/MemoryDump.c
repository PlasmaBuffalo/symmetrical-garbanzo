#include <stdio.h>
#include <stddef.h>

//This is as far as we got, had some trouble converting between numbers

//Dump method
void dump(char *sa, int nb)
{
    //pointer/address line
    printf("\n Pointer Line: %p ", &sa[0]);

    for (int i = 0; i < 8; i++)
    {
        //8 two-bit hex bits
        printf("%02hhx ", *(sa + i));
    }
    for (int i = 0; i < 8; i++)
    {
        //8 ASCII characters, if possible
        if (*(sa + i) > 32 && *(sa + i) < 126)
        {
            printf("%c ", *(sa + i));
        }

        //}else{printf(".");}
    }
    //
    printf("\n");
    //
    printf("\n");
}

//Main method
void main()
{
    //Declare array to store fibonaci numbers
    double fn[100];
    //Fibonacci

    int f1 = 0, f2 = 1, f3;
    for (int i = 0; i < 100; i++)
    {
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
        fn[i] = f1;
    }

    for (int i = 0; i < 100; i++){
        printf("\n%d ", fn[i]);
    }
    printf("\n");
    dump(fn, 100);
}