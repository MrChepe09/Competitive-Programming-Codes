#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        if (s.size() % 2 == 1)
        {
            cout << -1 << endl;
            continue;
        }
        int cnt = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == '1')
            {
                cnt++;
            }
        }
        if (cnt == s.size())
        {
            cout << -1 << endl;
        }
        else
        {
            cout << (s.size() / 2) - min(cnt, ((int)s.size() - cnt)) << endl;
        }
    }
}