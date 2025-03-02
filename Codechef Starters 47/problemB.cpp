#include <iostream>
#include <unordered_map>
#include <vector>
// #include <algorithm>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n;
        cin >> n;
        vector<int> arr(n);
        unordered_map<int, int> umap;
        int maximumHeight = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            umap[arr[i]]++;
            maximumHeight = max(maximumHeight, arr[i]);
        }
        int countOne = 0;
        int maximumCount = 0;
        for (auto it : umap)
        {
            if (it.second == 1)
                countOne++;
            maximumCount = max(maximumCount, it.second);
        }

        if (countOne % 2 == 0)
            cout << (int)(countOne / 2) << endl;
        else
        {
            int ans = (int)(countOne / 2) + 1;
            if (umap[maximumHeight] == 1 && maximumCount == 2)
                ans++;
            cout << ans << endl;
        }
    }
}