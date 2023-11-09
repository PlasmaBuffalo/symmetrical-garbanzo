#include <stdio.h>

//Declare variables needed in program

//array-based simulation of the simpletron memory
int memory[100];

//"Represents the accumulator register"
int accumulator = 0000;

//Goes down the list of input instructions; value is number of instruction
int instructionCounter = 00;

//Instructions are not executed directly from memory, this variable holds one at a time instead
int instructionRegister = 0000;

//First two digits of instructionRegister (operation to perform)
int operationCode = 00;

//Second two digits of instructionRegister (memory location)
int operand = 00;

//Method to perform a full memory dump
void memoryDump()
{
    for (int i = 0; i < 99; i = i + 10)
    {
        printf("%04d %04d %04d %04d %04d %04d %04d %04d %04d %04d", memory[i], memory[i + 1], memory[i + 2], memory[i + 3], memory[i + 4], memory[i + 5], memory[i + 6], memory[i + 7], memory[i + 8], memory[i + 9]);
        printf("\n");
    }
}

//Method to execute current instruction
void executeCurrent()
{
    //Set all relevant variables for current instruction execution cycle
    instructionRegister = memory[instructionCounter];
    operationCode = instructionRegister / 100;
    operand = instructionRegister % 100;

    /*
    printf("IC=%d - ", instructionCounter);
    printf("IR=%d - ", memory[instructionCounter]);
    printf("OC=%d - ", operationCode);
    printf("OP=%d\n", operand);
    */
    switch (operationCode)
    {
    case (10):
    {
        /* this is a read command */
        printf("READ\n");
        int readIn = 0;
        printf("reading...\n");
        scanf("%d", &readIn);
        memory[operand] = readIn;
    }
    case (11):
    {
        /* this is a write command */
        printf("%d", memory[operand]);
        printf("\n");
        break;
    }
    case (20):
    {
        /* this is a load command */
        accumulator = memory[operand];
        break;
    }
    case (21):
    {
        /* this is a store command */
        memory[operand] = accumulator;
        break;
    }
    case (30):
    {
        /* this is a add command */
        accumulator = accumulator + memory[operand];
        break;
    }
    case (31):
    {
        /* this is a subtract command */
        accumulator = accumulator - memory[operand];
        break;
    }
    case (32):
    {
        /* this is a divide command */
        accumulator = accumulator / memory[operand];
        break;
    }
    case (33):
    {
        /* this is a multiply command */
        accumulator = accumulator * memory[operand];
        break;
    }
    case (40):
    {
        /* this is a branch command */
        instructionCounter = operand;
        break;
    }
    case (41):
    {
        /* this is a branchNeg command */
        if (accumulator < 0)
        {
            instructionCounter = operand;
        }
        break;
    }
    case (42):
    {
        /* this is a branchZero command */
        if (accumulator == 0)
        {
            instructionCounter = operand;
        }
        break;
    }
    case (43):
    {
        /* this is a halt command */
        break;
    }
    default:
    {
        printf("*** Simpletron execution abnormally terminated ***\n");
        //memory dump
        memoryDump();
        break;
    }
    }
}

//Driver method
void main()
{
    //Intro statement
    printf("*** Welcome to Simpletron! ***\n");
    printf("*** Please enter your program one instruction ***\n");
    printf("*** (or data word) at a time. I will display ***\n");
    printf("*** the location number and a question mark (?) ***\n");
    printf("*** You then type the word for that location. ***\n");
    printf("*** Type -99999 to stop entering your program. ***\n");

    //initialize the array with zeroes
    for (int i = 0; i < 100; i++)
    {
        memory[i] = 0;
    }

    //Variable to determine final instruction location in memory (essentially relevant size of array)
    int last;
    //Loop through memory locations, taking user input until -99999 is entered
    for (int i = 0; i < 100; i++)
    {
        printf("%d", i);
        printf(" ? \n");
        int num;
        scanf("%d", &num);
        if (num == -99999)
        {
            break;
        }
        else if (num == 4300)
        {
            last = i;
        }
        else
        {
            memory[i] = num;
        }
    }

    printf("*** Program loading completed ***\n");
    printf("*** Program execution begins ***\n");

    //Run loop
    for (instructionCounter = 0; instructionCounter < last; instructionCounter++)
    {
        executeCurrent();
    }
}
