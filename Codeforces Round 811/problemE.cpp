#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;

int next(int x)
{
    return x + x % 10;
}

void solve()
{
    int n;
    cin >> n;
    vector<int> a(n);
    bool flag = false;
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
        if (a[i] % 5 == 0)
        {
            flag = true;
            a[i] = next(a[i]);
        }
    }
    if (flag)
    {
        cout << (*min_element(a.begin(), a.end()) == *max_element(a.begin(), a.end()) ? "Yes" : "No") << '\n';
    }
    else
    {
        bool flag2 = false, flag12 = false;
        for (int i = 0; i < n; ++i)
        {
            int x = a[i];
            while (x % 10 != 2)
            {
                x = next(x);
            }
            if (x % 20 == 2)
            {
                flag2 = true;
            }
            else
            {
                flag12 = true;
            }
        }
        cout << ((flag2 & flag12) ? "No" : "Yes") << '\n';
    }
}

int main()
{
    int t = 1;
    cin >> t;
    for (int it = 0; it < t; ++it)
    {
        solve();
    }
    return 0;
}