#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef long long int ll;

bool possible = 1;

void dfs(vector<ll> edges[], vector<bool> &vis, vector<bool> &col, ll v, bool c)
{
    if (vis[v])
        return;

    vis[v] = 1;
    col[v] = c;

    for (ll child : edges[v])
    {
        if (!vis[child])
        {
            dfs(edges, vis, col, child, c ^ 1);
        }
        else
        {
            if (c == col[child])
            {
                possible = 0;
            }
        }
    }
}

int main()
{
    ll n, m;
    cin >> n >> m;
    vector<ll> edges[n];
    vector<bool> vis(n, false);
    vector<bool> color(n, false);
    for (ll i = 0; i < m; i++)
    {
        ll u, v;
        cin >> u >> v;
        --u, --v;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }

    for (ll i = 0; i < n; i++)
        if (!vis[i])
            dfs(edges, vis, color, i, 0);

    if (possible)
    {
        ll cnt[2] = {0};
        for (ll i = 0; i < n; i++)
            ++cnt[color[i]];

        cout << cnt[0] << endl;
        for (ll i = 0; i < n; i++)
            if (color[i] == 0)
                cout << i + 1 << " ";
        cout << endl;

        cout << cnt[1] << endl;
        for (ll i = 0; i < n; i++)
            if (color[i] == 1)
                cout << i + 1 << " ";
        cout << endl;
    }
    else
    {
        cout << -1 << endl;
    }
}