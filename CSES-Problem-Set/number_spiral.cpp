#include <iostream>
using namespace std;

int main()
{
    long long t;
    cin >> t;
    while (t--)
    {
        long long a, b;
        cin >> a >> b;
        long long maxi = max(a, b);
        long long start = (maxi * maxi) - (maxi - 1);
        if (a == b)
        {
            cout << start << endl;
        }
        else
        {
            if (maxi % 2 != 0)
            {
                if (a < b)
                {
                    while (b != a)
                    {
                        start++;
                        b--;
                    }
                }
                else
                {
                    while (a != b)
                    {
                        start--;
                        a--;
                    }
                }
                cout << start << endl;
            }
            else
            {
                if (a < b)
                {
                    while (b != a)
                    {
                        start--;
                        b--;
                    }
                }
                else
                {
                    while (a != b)
                    {
                        start++;
                        a--;
                    }
                }
                cout << start << endl;
            }
        }
    }
}