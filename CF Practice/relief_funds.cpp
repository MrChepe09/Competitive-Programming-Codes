#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
int total = 0, c = 0;
vector<int> arr(10001);
vector<int> gra[10001];
int vis[10001];
vector<int> ans;

int dfs(int node)
{
    total += arr[node];
    c++;
    vis[node] = 1;
    for (int child : gra[node])
    {
        if (!vis[child])
        {
            dfs(child);
        }
    }
}
int dfs2(int node)
{
    ans.push_back(node);
    vis[node] = 3;
    for (int child : gra[node])
    {
        if (vis[child] != 3)
        {
            dfs2(child);
        }
    }
}

int main()
{
    int maxi = -1;
    int it = 0;
    int size = 100001;
    int n;
    cin >> n;

    for (int i = 0; i <= n; i++)
    {
        vis[i] = 0;
    }
    for (int i = 1; i <= n; i++)
    {
        cin >> arr[i];
    }
    int m, b, a;
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        gra[a].push_back(b);
        gra[b].push_back(a);
    }

    for (int i = 1; i <= n; i++)
    {
        if (vis[i] != 1)
        {
            dfs(i);
            if (total > maxi)
            {
                maxi = max(maxi, total);
                it = i;
                size = c;
            }
            else if (total == maxi)
            {
                if (size > c)
                {
                    it = i;
                    size = c;
                }
            }
            total = 0;
            c = 0;
        }
    }
    dfs2(it);
    sort(ans.begin(), ans.end());
    for (int i = 0; i < ans.size(); i++)
    {
        if (i == ans.size() - 1)
        {
            cout << ans[i];
        }
        else
        {
            cout << ans[i] << " ";
        }
    }
}