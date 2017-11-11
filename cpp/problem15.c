#include <stdio.h>
#include <math.h>

#define TRUE 1
#define SIDELEN 20
#define COUNT SIDELEN*2
#define START pow(2,SIDELEN)
#define MAX pow(2,COUNT)+1-START

int checkeven(int n)
{
    int t;
    t = 0;
    while (n>0)
    {
        t = t + (n % 2);
        n = n >> 1;
    }
    if (t == SIDELEN) { return TRUE; }
    
    return 0;
}

int main(void)
{
    long t = 0;
    long i = START-1;
    
    while (i < MAX)
    {
        if (checkeven(i) == TRUE)
        {
            t++;
        }
        i++;
    }
    
    printf("%d\n",t);
    
    return 0;
}

