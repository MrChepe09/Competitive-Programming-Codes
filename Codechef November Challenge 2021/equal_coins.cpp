#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int x, y;
        cin >> x >> y;
        if (x % 2 != 0)
        {
            cout << "NO" << endl;
        }
        else
        {
            if ((x % 2 == 0 && y % 2 == 0))
            {
                cout << "YES" << endl;
            }
            else if (y % 2 != 0 && x >= 2)
            {
                cout << "YES" << endl;
            }
            else
            {
                cout << "NO" << endl;
            }
        }
    }
}