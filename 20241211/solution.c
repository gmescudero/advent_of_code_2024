
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define BLINKS (75)


int *stones = NULL;

int countDigits(int num)
{
    int numberOfDigits = 0;
    while (num != 0)
    {
        numberOfDigits++;
        num /= 10;
    }
    return numberOfDigits;
}

void blink(int in, int *numberOfOuts, int *out1, int *out2)
{
    int base = 0;
    *numberOfOuts = 1;

    if (0 == in)
    {
        *out1 = 1;
        return;
    }
    int digitsNum = countDigits(in);
    if (digitsNum % 2 == 0)
    {
        *numberOfOuts=2;
        int base = pow(10,digitsNum/2);
        *out1 = in/base;
        *out2 = in - ((*out1)*base);
    }
    else
    {
        *out1 = in * 2024;
    }
}


int main(void)
{
    printf("Allocating stones size\n");
    stones = (int*)malloc(1e10);

    const int blinksNum = BLINKS;
    int stonesNum = 2;

/*     
    stones[0] = 125;
    stones[1] = 17;
 */

    stones[0] = 70949;
    stones[1] = 6183;
    stones[2] = 4;
    stones[3] = 3825336;
    stones[4] = 613971;
    stones[5] = 0;
    stones[6] = 15;
    stones[7] = 182;


    for (int i = 0; i < blinksNum; i++)
    {
        for (int st = stonesNum-1; st >= 0; st--)
        {
            int newSt1 = 0, newSt2 = 0; 
            int newNum = 0;
            blink(stones[st], &newNum, &newSt1, &newSt2);
            stones[st] = newSt1;
            if (newNum == 2)
            {
                stones[stonesNum] = newSt2;
                stonesNum++;
            }
        }
        printf("Blinked %d out of %d times\n",i+1, blinksNum);
        // printf("\t -> ");
        // for (int j = 0; j < stonesNum; j++) printf("%d, ",stones[j]);
        // printf("\n");
    }

    printf("Total stones number: %d\n",stonesNum);

    return 0;
}