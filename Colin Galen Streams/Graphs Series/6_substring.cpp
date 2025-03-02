#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cstring>
using namespace std;

typedef long long int ll;

vector<ll> edges[300005];
ll indegree[300005];
vector<ll> toposort;
ll dp[300005];

int main()
{
    ll n, m;
    cin >> n >> m;

    string s;
    cin >> s;
    for (ll i = 0; i < m; i++)
    {
        ll u, v;
        cin >> u >> v;
        --u, --v;
        edges[u].push_back(v);
        ++indegree[v];
    }

    queue<ll> q;
    ll cnt = 0;
    for (ll i = 0; i < n; i++)
    {
        if (indegree[i] == 0)
            q.push(i);
    }

    while (!q.empty())
    {
        ++cnt;
        ll x = q.front();
        q.pop();
        toposort.push_back(x);

        for (ll y : edges[x])
        {
            --indegree[y];

            if (indegree[y] == 0)
                q.push(y);
        }
    }

    if (cnt < n)
    {
        cout << -1 << endl;
    }
    else
    {
        ll ans = 0;
        for (char c = 'a'; c <= 'z'; c++)
        {
            memset(dp, 0, sizeof(dp));

            for (ll x : toposort)
            {
                if (s[x] == c)
                    ++dp[x];
                for (ll y : edges[x])
                {
                    dp[y] = max(dp[y], dp[x]);
                }
                ans = max(ans, dp[x]);
            }
        }
        cout << ans << endl;
    }
}