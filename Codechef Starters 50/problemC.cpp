#include <iostream>
#include <vector>
using namespace std;

typedef long long int ll;

bool solve(ll x, ll y)
{
    for (ll i = 1; i * i <= y; i++)
    {
        if (y % i == 0)
        {
            vector<ll> firstSeq{i, y / i};

            vector<ll> secSeg{-1, -1};
            secSeg[0] = min(firstSeq[0], firstSeq[1]) - 1;
            secSeg[1] = x - secSeg[0];

            if (secSeg[1] <= secSeg[0])
            {
                if (secSeg[1] < 0)
                {
                    secSeg[0] = x;
                    secSeg[1] = 0;
                }
                cout << min(firstSeq[0], firstSeq[1]) << " " << max(firstSeq[0], firstSeq[1]) << endl;
                cout << min(secSeg[0], secSeg[1]) << " " << max(secSeg[0], secSeg[1]) << endl;
                return true;
            }

            secSeg[0] = max(firstSeq[0], firstSeq[1]) + 1;
            secSeg[1] = x - secSeg[0];

            if (secSeg[1] > max(firstSeq[0], firstSeq[1]))
            {
                cout << min(firstSeq[0], firstSeq[1]) << " " << max(firstSeq[0], firstSeq[1]) << endl;
                cout << min(secSeg[0], secSeg[1]) << " " << max(secSeg[0], secSeg[1]) << endl;
                return true;
            }
        }
    }
    return false;
}

int main()
{
    ll test;
    cin >> test;
    while (test--)
    {
        ll x, y;
        cin >> x >> y;
        bool possible = solve(x, y);

        if (!possible)
        {
            cout << -1 << endl;
        }
    }
}