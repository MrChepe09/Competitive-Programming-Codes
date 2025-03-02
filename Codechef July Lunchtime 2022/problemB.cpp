#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        bool possible = true;
        unordered_map<char, int> umap;
        for (int i = 0; i < s.size(); i += 2)
        {
            umap[s[i]]++;
        }
        for (int i = 1; i < s.size(); i += 2)
        {
            if (umap.find(s[i]) == umap.end())
            {
                possible = false;
                break;
            }
            else
            {
                if (umap[s[i]] == 0)
                {
                    possible = false;
                    break;
                }
                else
                {
                    umap[s[i]]--;
                }
            }
        }
        for (auto it : umap)
        {
            if (it.second != 0)
            {
                possible = false;
            }
        }
        (possible) ? cout << "YES" << endl : cout << "NO" << endl;
    }
}