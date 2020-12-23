#include <iostream>
// #include <stdlib.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        long long x, y, k, n;
        cin >> x >> y >> k >> n;
        if ((abs(x - y)) % k == 0 && (abs(x - y) / k) % 2 == 0)
        {
            cout << "Yes" << endl;
        }
        else
        {
            cout << "No" << endl;
        }
    }
}