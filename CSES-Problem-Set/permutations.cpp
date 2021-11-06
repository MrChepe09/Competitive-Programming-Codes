#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    if (n == 1)
    {
        cout << "1" << endl;
    }
    else if (n <= 3)
    {
        cout << "NO SOLUTION" << endl;
    }
    else if (n == 4)
    {
        cout << "3 1 4 2" << endl;
    }
    else
    {
        int first = 1;
        int second = 2;
        cout << first;
        first += 2;
        while (first <= n)
        {
            cout << " " << first;
            first += 2;
        }
        while (second <= n)
        {
            cout << " " << second;
            second += 2;
        }
    }
}