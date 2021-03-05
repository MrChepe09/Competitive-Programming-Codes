#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        string s = "";
        if (n > k)
        {
            cout << -1 << endl;
            continue;
        }
        else if (n == k)
        {
            for (int i = 0; i < n; i++)
            {
                s += 'a';
            }
            cout << s << endl;
            continue;
        }
        else
        {
            int i = 1;
            while (i <= 25)
            {
                if (k - pow(2, i) == n - 1)
                {
                    char symbol = (char)('a' + i);
                    s += symbol;
                }
                i++;
            }
            for (int i = 0; i < n - 1; i++)
            {
                s += 'a';
            }

            cout << s << endl;
        }
    }
}