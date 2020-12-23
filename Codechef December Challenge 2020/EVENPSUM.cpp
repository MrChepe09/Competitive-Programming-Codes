#include <iostream>
using namespace std;

void evenoddsum()
{
    long long a, b;
    long long o1, e1, o2, e2;
    cin >> a >> b;
    if (a % 2 == 1)
    {
        o1 = (a / 2) + 1;
        e1 = (a / 2);
    }
    else
    {
        o1 = a / 2;
        e1 = a / 2;
    }

    if (b % 2 == 1)
    {
        o2 = (b / 2) + 1;
        e2 = (b / 2);
    }
    else
    {
        o2 = b / 2;
        e2 = b / 2;
    }
    cout << (o1 * o2) + (e1 * e2) << '\n';
}

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        evenoddsum();
    }
}