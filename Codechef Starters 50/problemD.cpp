#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
typedef long long int ll;

int main()
{
    ll test;
    cin >> test;
    while (test--)
    {
        ll n, x, y;
        cin >> n >> x >> y;

        vector<ll> arr(n);
        ll maxi = 0;
        for (ll i = 0; i < n; i++)
        {
            cin >> arr[i];
            maxi = max(maxi, arr[i]);
        }
        ll ans = 0;
        if (y >= x)
        {
            ans = ceil((double)maxi / (double)y);
        }
        else
        {
            ll num = 0;
            for (ll i = n - 1; i >= 0; i--)
            {
                if (arr[i] - num > 0)
                {
                    ans += ceil((double)(arr[i] - num) / (double)x);
                    num += ceil((double)(arr[i] - num) / (double)x) * y;
                }
            }
        }
        cout << ans << endl;
    }
}