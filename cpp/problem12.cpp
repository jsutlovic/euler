#include <cmath>
#include <iostream>

using namespace std;

int ndiv = 500;

int nfactors( int n )
{
    int lim = (int)sqrt(n);
    int f = 0;

    for (int i=1; i<=lim; i++)
    {
        if (n%i==0)
        {
            f+=2;
        }
    }
    return f;
}


int main()
{
    int t = 1;
    int i = 2;

    while (true)
    {
        if ( nfactors(t) > ndiv ) break;

        t += i;
        i++;
    }

    cout << t << endl;

    return 0;
}
