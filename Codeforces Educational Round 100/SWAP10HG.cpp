#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string s, p;
        cin >> s;
        cin >> p;
        int one = 0, one1 = 0;
        for (int i = 0; i < n; i++)
        {
            if (s[i] == '1')
            {
                one++;
            }
        }
        for (int i = 0; i < n; i++)
        {
            if (p[i] == '1')
            {
                one1++;
            }
        }
        if (one != one1)
        {
            cout << "No" << endl;
        }
        else if (s == p)
        {
            cout << "Yes" << endl;
        }
        else
        {
            int res = 0;
            one = 0;
            for (int i = 0; i < n; i++)
            {
                if (s[i] == '1' && p[i] == '0')
                {
                    one++;
                }
                else if (s[i] == '0' && p[i] == '1')
                {
                    one--;
                    if (one < 0)
                    {
                        res = 1;
                        break;
                    }
                }
            }
            if (res == 1)
            {
                cout << "No" << endl;
            }
            else
            {
                cout << "Yes" << endl;
            }
        }
    }
}