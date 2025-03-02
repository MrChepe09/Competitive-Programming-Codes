#include <iostream>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n, m;
        cin >> n >> m;
        int area = n * m;
        int twoBytwo = 0;

        if (n < m)
        {
            while (n >= 2)
            {
                twoBytwo += (m / 2);
                n -= 2;
            }
        }
        else
        {
            while (m >= 2)
            {
                twoBytwo += (n / 2);
                m -= 2;
            }
        }
        // cout << twoBytwo << endl;
        cout << (area) - (4 * twoBytwo) << endl;
    }
}