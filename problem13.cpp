#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <fstream>
#include <string>
#include <deque>

using namespace std;

#define NUMS 100
#define COLS 50

int numbers[NUMS][COLS];
int sum10[10];

void getnums( string fname )
{
    int row = 0;
    ifstream numfile;
    numfile.open( fname.c_str() );
    string line;

    if (numfile.is_open())
    {
        while ( numfile.good() )
        {
            getline( numfile, line );
            for ( int i=0; i<COLS; i++ )
            {
                numbers[row][i] = (int)(line[i]-0x30);
            }

            row++;
        }
        numfile.close();
    }
    else cout << "Unable to open file" << endl;
}

string strnum( int * nums, int len )
{
    string s;

    for (int i=0; i<len; i++)
    {
        s.push_back((char)(nums[i]+0x30));
    }

    return s;
}

string strnum( deque<int> nums )
{
    string s;

    for (deque<int>::iterator i=nums.begin(); i!=nums.end(); i++)
    {
        s.push_back((char)(*i+0x30));
    }

    return s;
}

int *sumnums()
{
    deque<int> sum;

    int cursum = 0;
    int i = COLS-1;

    while (true)
    {
        if (i>=0)
        {
            for (int j=NUMS-1; j>=0; j--)
            {
                cursum += numbers[j][i];
            }
            i--;
        }

        sum.push_front( cursum % 10 );
        cursum/=10;
        if (cursum == 0) break;
    }

    for (int i=0; i<10; i++)
    {
        sum10[i] = sum[i];
    }

    //cout << strnum (sum) << endl;

    return sum10;
}


int main()
{
    getnums("problem13.txt");

    cout << strnum(sumnums(), 10) << endl;

    return 0;
}
