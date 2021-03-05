#include <iostream>
using namespace std;
typedef long long ll;

int main()
{
    ll n;
    cin >> n;
    ll arr[n];
    for (ll i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    ll res = 0;
    for (ll i = 1; i < n; i++)
    {
        if (arr[i] < arr[i - 1])
        {
            res += (arr[i - 1] - arr[i]);
            arr[i] = arr[i - 1];
        }
    }
    cout << res << endl;
}