#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v;
    string str;
    cin >> str;
    stringstream ss(str);
    unordered_map<int, int> umap;
    int find;
    cin >> find;
    while (ss.good())
    {
        string substr;
        getline(ss, substr, ',');
        stringstream sss(substr);
        int x;
        sss >> x;
        v.push_back(x);
    }

    for (int i = 0; i < v.size(); i++)
    {
        umap[v[i]] += 1;
    }
    int flag = 0;
    for (int i = 0; i < v.size(); i++)
    {
        if (umap.find(find - v[i]) != umap.end())
        {
            if (v[i] == find - v[i])
            {
                if (umap[v[i]] > 2)
                {
                    cout << 1;

                    flag = 1;
                    break;
                }
            }
            else
            {
                cout << 1;
                flag = 1;
                break;
            }
        }
    }
    if (flag == 0)
    {
        cout << 0;
    }
}