#include <iostream>
#include <vector>
using namespace std;

typedef long long int ll;

vector<ll> edges[150005];
ll label[150005];  // current component of each vertex
ll sz[1500005];    // size of each component (labels)
ll nedges[150005]; // number of edges in each component

void relabel(ll v, ll target)
{
    // relabel vertex v and neighbours to target
    if (label[v] == target)
        return;
    label[v] = target;

    for (ll x : edges[v])
    {
        relabel(x, target);
    }
}

void merge(ll u, ll v)
{
    edges[u].push_back(v);
    edges[v].push_back(u);
    ll cu = label[u];
    ll cv = label[v];
    ++nedges[cu];

    if (cu == cv)
        return;

    if (sz[cu] > sz[cv])
        swap(u, v), swap(cu, cv);

    // assume sz[cu] <= sz[cv]
    relabel(u, cv);

    sz[cv] += sz[cu];
    nedges[cv] += nedges[cu];
}

int main()
{
    ll n, m;
    cin >> n >> m;

    for (ll i = 0; i < n; i++)
    {
        sz[i] = 1;
        label[i] = i;
    }
    for (ll i = 0; i < m; i++)
    {
        ll u, v;
        cin >> u >> v;
        --u;
        --v;
        merge(u, v);
    }

    bool possible = true;
    for (ll i = 0; i < n; i++)
    {
        if (nedges[label[i]] != sz[label[i]] * (sz[label[i]] - 1) / 2)
            possible = false;
    }

    cout << (possible ? "YES" : "NO") << endl;
}