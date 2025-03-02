#include <iostream>
#include <set>
using namespace std;

typedef long long ll;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n, x;
        cin >> n >> x;

        ll maxNum = 0;
        for (ll i = 20; i >= 0; i--)
        {
            if (n & (1 << i))
            {
                maxNum = (1 << (i + 1));
                break;
            }
        }

        if ((n == 2 && x != 3) || (x >= maxNum) || ((n & (n - 1)) == 0 && (x & n) == 0))
        {
            cout << -1 << endl;
            continue;
        }
        if (n == 2)
        {
            cout << "1 1 2" << endl;
            continue;
        }

        set<ll> arr1;
        for (int i = 1; i <= n; ++i)
        {
            arr1.insert(i);
        }

        set<ll> arr2;
        for (int i = 0; i <= 20; ++i)
        {
            ll num = (1 << i);
            if (num > n)
                break;

            if ((x & num) == 0)
            {
                arr1.erase(num);

                arr2.insert(num);
            }
        }

        ll num = 0;
        if (arr1.size() > 0)
        {
            num = *arr1.begin();
            arr1.erase(num);
            for (auto i : arr1)
            {
                cout << "1 " << num << " " << i << endl;
                num = num | i;
            }
        }

        ll comp = 0;
        if (arr2.size() > 0)
        {
            comp = *arr2.begin();
            arr2.erase(comp);
            for (auto i : arr2)
            {
                cout << "1 " << comp << " " << i << endl;
                comp = comp | i;
            }
        }

        if (num > 0 && comp > 0)
        {
            cout << "2 " << num << " " << comp << endl;
        }
    }
}