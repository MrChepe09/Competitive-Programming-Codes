// Problem Link:- https://codeforces.com/contest/237/problem/A

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    unordered_map<string, int> ul;
    int count = 1;
    for (int i = 0; i < n; i++)
    {
        string h, m;
        cin >> h >> m;
        string f = h + m;
        if (ul.find(f) != ul.end())
        {
            ul[f]++;
        }
        else
        {
            ul[f] = 1;
        }
    }
    for (auto x : ul)
    {
        count = max(count, x.second);
    }
    cout << count;
}