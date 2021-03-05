#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
    string s;
    cin >> s;
    ll l = s.length();
    char c;
    ll count, max = 1;

    for (ll i = 0; i < l - 1;)
    {
        c = s[i];

        count = 1;
        for (ll j = i + 1; j < l; j++)
        {
            if (c == s[j])
                ++count;
            else
                break;
        }
        if (count >= max)
            max = count;

        i = i + count;
    }
    cout << max << endl;
}