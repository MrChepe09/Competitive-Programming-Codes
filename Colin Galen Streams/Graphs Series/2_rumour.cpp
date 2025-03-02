#include <iostream>
#include <vector>
using namespace std;

typedef long long int ll;

ll dfs(vector<ll> graph[], vector<ll> &arr, vector<bool> &visited, ll &cost, ll curr)
{
    visited[curr] = true;
    cost = min(cost, arr[curr - 1]);

    for (ll child : graph[curr])
    {
        if (!visited[child])
            dfs(graph, arr, visited, cost, child);
    }
    return cost;
}

int main()
{
    ll n, m;
    cin >> n >> m;
    vector<ll> arr(n);
    for (ll i = 0; i < n; i++)
        cin >> arr[i];
    vector<ll> graph[n + 1];
    for (ll i = 0; i < m; i++)
    {
        ll a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    vector<bool> visited(n + 1, false);

    ll cost = 0;
    for (ll i = 1; i <= n; i++)
    {
        if (!visited[i])
        {
            cost += dfs(graph, arr, visited, arr[i - 1], i);
        }
    }
    cout << cost << endl;
}