#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;


/* ProjectEuler.net */


//Problem 1
int problem1() {
    int total = 0;

    for (int i = 0; i < 1000; i++) {
        if (i%3==0 || i%5==0){
            total += i;
        }
    }

    return total;
}


//Problem 2
int problem2(int maxfib) {
    int fib1 = 1;
    int fib2 = 2;
    int total = 0;

    while (fib2 < maxfib) {
        //Switch fib1 and fib2 in-place;
        fib2 = fib1+fib2;
        fib1 = fib2-fib1;
        if (fib1%2==0) {
            total += fib1;
        }
    }
    return total;
}


//Problem 3
bool is_prime(long long x){
    for (int i=2; i <= (int) sqrt(x); i++) {
        if (x%i==0)
            return false;
    }
    return true;
}

bool is_prime( int x ){
    for (int i=2; i<=(int) sqrt(x); i++) {
        if (x%i==0)
            return false;
    }
    return true;
}

int problem3(long long x) {
    int biggest = 1;

    for (int i=1; i < (int) sqrt(x); i+=2) {
        if ( x%i==0 && is_prime(i) && biggest < i ) {
            biggest = i;
        }
    }

    return biggest;
}


// Problem 4
bool is_palindrome(int x) {
    int orig = x;
    int rev = 0;

    while (orig != 0) {
        rev = rev*10+orig%10;
        orig = orig/10;
    }

    return x == rev;
}

int problem4() {
    int biggest = 0;
    int sum = 0;
    for (int i=999; i > 100; i--) {
        for (int j=999; j > 100; j--) {
            sum = i*j;
            if (is_palindrome(sum) && biggest < sum) {
                biggest = sum;
            }
        }
    }
    return biggest;
}


//Problem 5
bool divall (int n, long long total){
    for (int i = 1; i<=n; i++) {
        if ((total%i)!=0) {
            return false;
        }
    }
    return true;
}

long long problem5(int n) {
    long long big = 1;
    for (int i=1; i<=n; i++) {
        big = big*i;
    }

    for (int i = n; i > 0; i--) {
        if (divall(n, big/i)) {
            big = big/i;
        }
    }

    return big;
}


//Problem 6
long long problem6 (int n) {
    //
    long long sumsquares = 0;
    long long squaresum = 0;

    for (int i=1; i<=n; i++) {
        sumsquares += pow(i, 2);
    }

    for (int i=1; i<=n; i++) {
        squaresum += i;
    }
    squaresum = pow(squaresum, 2);

    return squaresum - sumsquares;
}


//Problem 7
int problem7( int n ) {
    int primes[n];
    int primecount = 0;
    int i = 3;
    primes[0] = 2;

    while (primecount < n) {
        for ( int j=0; j <= primecount; j++){
            if (i%primes[j]==0) break;
            else if (j==primecount) {
                primecount++;
                primes[primecount] = i;
            }
        }
        i += 2;
    }

    return primes[n-1];
}


//Problem 8
int proddigits ( string substr ) {
    int total = 1;
    int sub = atoi(substr.c_str());
    while (sub>0) {
        total *= sub%10;
        sub /= 10;
    }
    return total;
}

int problem8() {
    int biggest = 0;
    int prod = 0;
    string text = "73167176531330624919225119674426574742355349194934"
                  "96983520312774506326239578318016984801869478851843"
                  "85861560789112949495459501737958331952853208805511"
                  "12540698747158523863050715693290963295227443043557"
                  "66896648950445244523161731856403098711121722383113"
                  "62229893423380308135336276614282806444486645238749"
                  "30358907296290491560440772390713810515859307960866"
                  "70172427121883998797908792274921901699720888093776"
                  "65727333001053367881220235421809751254540594752243"
                  "52584907711670556013604839586446706324415722155397"
                  "53697817977846174064955149290862569321978468622482"
                  "83972241375657056057490261407972968652414535100474"
                  "82166370484403199890008895243450658541227588666881"
                  "16427171479924442928230863465674813919123162824586"
                  "17866458359124566529476545682848912883142607690042"
                  "24219022671055626321111109370544217506941658960408"
                  "07198403850962455444362981230987879927244284909188"
                  "84580156166097919133875499200524063689912560717606"
                  "05886116467109405077541002256983155200055935729725"
                  "71636269561882670428252483600823257530420752963450";

    for (int i=0; i<1000-5; i++){
        prod = proddigits(text.substr(i, 5));
        if (prod > biggest){
            biggest = prod;
        }
    }

    return biggest;
}


//Problem 9
int problem9( int n ) {
    double k;
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=n; j++) {
            k = sqrt(pow(i,2)+pow(j,2));
            if (k==(int)k && (i+j+(int)k)==n)
                return i*j*k;
        }
    }
    return 0;
}


//Problem 10
long long problem10( int n ) {
    long long sum = 2;

    for (int i=3; i<=n; i+=2)
    {
        if (is_prime(i))
            sum+=i;
    }

    return sum;
}

long long problem10_2( int n ) {
    long long sum = 2;
    int half = ((n+1)/2)-1;

    int *pprimes;
    pprimes = (int*) malloc(4*half);

    for (int i=3, j=0; i<=n; i+=2,j++) {
        pprimes[j] = i;
    }

    int j,mroot;
    mroot = pow(n, 0.5);

    for (int i=0,m=3; m<=mroot;i++,m=2*i+3){
        if (pprimes[i]!=0) {
            j = (int) ((m*m-3)/2);
            pprimes[j] = 0;
            for (; j<half; j+=m){
                pprimes[j] = 0;
            }
        }
    }

    int numprime = 0;
    for (int i=0; i<half; i++){
        sum += pprimes[i];
        if (pprimes[i]!=0)
            numprime++;
    }

    return sum;
}

long long problem10_3( int n ){
    long long sum = 2;
    int half = ((n+1)/4);
    int sq;

    int *primes = (int *) malloc(4*half);
    primes[0]=2;
    unsigned int nprimes = 1;

    for (int i=3;i<=n; i+=2)
    {
        sq = (int)sqrt(i);
        for ( int j=0; j < nprimes; j++ )
        {
            if (i%primes[j]==0) break;
            else if (primes[j]>sq || j == nprimes-1)
            {
                //cout << "i: " << i << " j: " << j << " nprimes: " << nprimes << endl;
                primes[nprimes] = i;
                sum += i;
                nprimes++;
                break;
            }
        }
    }

    return sum;
}

long long problem10_4( int n )
{
    long long sum = 2;
    vector<int> primes;
    primes.push_back(2);

    for ( int i=3; i<=n; i+=2 )
    {
        for ( vector<int>::iterator j=primes.begin(); j!=primes.end(); j++ )
        {
            if ( i % *j == 0 ) break;
            else if ( *j > (int)sqrt(i) )
            {
                primes.push_back(i);
                sum += i;
                break;
            }
        }
    }

    return sum;
}


int main()
{
    /*cout << "Problem 1:  " << problem1() << endl;
    cout << "Problem 2:  " << problem2(4000000) << endl;
    cout << "Problem 3:  " << problem3(600851475143) << endl;
    cout << "Problem 4:  " << problem4() << endl;
    cout << "Problem 5:  " << problem5(20) << endl;
    cout << "Problem 6:  " << problem6(100) << endl;
    cout << "Problem 7:  " << problem7(10001) << endl;
    cout << "Problem 8:  " << problem8() << endl;
    cout << "Problem 9:  " << problem9(1000) << endl;*/
    cout << "Problem 10: " << problem10_3(2000000) << endl;
}



