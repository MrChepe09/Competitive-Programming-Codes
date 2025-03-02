#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef long long int ll;

vector<ll> bfs(vector<ll> edges[], vector<bool> &vis, ll i)
{
    vector<ll> comp;

    queue<ll> q;
    q.push(i);

    while (!q.empty())
    {
        ll x = q.front();
        q.pop();
        if (vis[x])
            continue;
        vis[x] = true;
        comp.push_back(x);

        for (ll y : edges[x])
            if (!vis[y])
                q.push(y);
    }
    return comp;
}

int main()
{
    ll n, m;
    cin >> n >> m;
    vector<ll> edges[n + 1];
    vector<bool> vis(n + 1, false);
    vector<ll> ans(n, 0);
    for (ll i = 0; i < m; i++)
    {
        ll k;
        cin >> k;
        vector<ll> v(k);
        for (ll j = 0; j < k; j++)
            cin >> v[j], --v[j];

        for (ll j = 0; j + 1 < k; j++)
        {
            edges[v[j]].push_back(v[j + 1]);
            edges[v[j + 1]].push_back(v[j]);
        }
    }

    for (ll i = 0; i < n; i++)
    {
        if (!vis[i])
        {
            vector<ll> comp = bfs(edges, vis, i);
            for (ll x : comp)
                ans[x] = comp.size();
        }
    }
    for (ll i : ans)
    {
        cout << i << " ";
    }
}