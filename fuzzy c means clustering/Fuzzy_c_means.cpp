#include<cstdio>
#include<iostream>
#include<cmath>

#define N 10
#define C 2
#define m 5
#define ITER 3

using namespace std;

/*********** Fuzzy c-means clustering for one dimensional data ***************/

double u[N][C];
double c[C];
double x[N];

double euclidean_sq(double x,double y)
{
    return ((x-y)*(x-y));
}

double euclidean(double x,double y)
{
    return sqrt((x-y)*(x-y));
}


double update_membership(int i,int j)
{
    double value = 0.0;
    double t = m-1;
    double exp = 2.0/t;
    double numerator = euclidean(x[i],c[j]);

    for(int k=0;k<C;k++)
    {
        double denominator = euclidean(x[i],c[k]);
        value = value + pow((numerator/denominator),exp);
    }
    return (1/value);
}

double update_center(int j)
{
    double numerator = 0.0;
    double denominator = 0.0;

    for(int i=0;i<N;i++)
    {
        numerator = numerator + (u[i][j]*x[i]); // It is a dot-product - one dimensional data point in this case
        denominator = denominator + u[i][j];
    }
    return (numerator/denominator);
}

void flush()
{
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<C;j++)
        {
            u[i][j] = 0.0;
            c[j] = 0.0;
        }
    }
    return;
}

void print_center()
{
    for(int j=0;j<C;j++)
    {
        cout <<"Center : "<<c[j] << endl;
    }
    return;
}

void print_membership()
{
    for(int i=0;i<N;i++)
    {
        cout << " Class c1: " << u[i][0] << " Class c2: "<< u[i][1]<< endl;
    }
    return;
}
int main()
{
    flush();
    /************* Initialize ****************/
    u[0][1] = 0.8;
    u[0][2] = 0.2;
    u[1][1] = 0.3;
    u[1][2] = 0.7;
    u[2][1] = 0.6;
    u[2][2] = 0.4;
    u[3][1] = 0.5;
    u[3][2] = 0.5;
    u[4][1] = 0.4;
    u[4][2] = 0.6;
    u[5][1] = 0.3;
    u[5][2] = 0.7;
    u[6][1] = 0.2;
    u[6][2] = 0.8;
    u[7][1] = 0.1;
    u[7][2] = 0.9;
    u[8][1] = 0.9;
    u[8][2] = 0.1;
    u[9][1] = 0.9;
    u[9][2] = 0.1;
    x[0] = 8;
    x[1] = 22;
    x[2] = 32;
    x[3] = 48;
    x[4] = 56;
    x[5] = 60;
    x[6] = 72;
    x[7] = 87;
    x[8] = 3;
    x[9] = 98;


 print_membership();
 print_center();

    for(int t=0;t<ITER;t++)
    {
        for(int j=0;j<C;j++)
        {
            c[j] = update_center(j);
        }
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<C;j++)
            {
                u[i][j] = update_membership(i,j);
            }
        }
    }
print_membership();
print_center();




    return 0;
}
