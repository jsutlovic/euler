#include <cstdlib>
#include <iostream>

using namespace std;

#define M 1000000
#define LIM M

short *numbers = (short *)calloc( LIM,sizeof(short) );

int getchainlen( long long n )
{
    if ( n == 1 ) return 1;

    /* Slow, inefficient
    if ( n%2==0 ) return (1+getchainlen( n/2 ));
    else          return (1+getchainlen( 3*n+1 ));
    */

    if ( n < LIM && numbers[n]!=0 )
    {
        return (int)numbers[n];
    }
    else
    {
        short steps;
        if ( n%2==0 ) steps = (1+getchainlen( n/2 ));
        else          steps = (1+getchainlen( 3*n+1 ));
        if ( n < LIM ) numbers[n] = steps;
        return (int)steps;
    }
}

int getbiggest( int lim )
{
    int biggest = 0;
    int biggestamt = 0;
    int il;

    for ( int i=3; i<lim; i++ )
    {
        il = getchainlen(i);
        if ( il>biggestamt )
        {
            biggest = i;
            biggestamt = il;
        }
    }

    return biggest;
}


int main()
{
    numbers[1] = 1;
    numbers[2] = 2;
    int big = getbiggest( M );

    cout << "num: " << big << endl;
    cout << "len: " << getchainlen( big ) << endl;
    return 0;
}
