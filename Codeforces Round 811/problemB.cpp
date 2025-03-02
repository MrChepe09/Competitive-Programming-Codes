#include <iostream>
#include <vector>
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
        vector<int> arr(n);
        unordered_map<int, int> umap;
        int ans = 0;
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        for (int i = n - 1; i >= 0; i--)
        {
            if (umap.find(arr[i]) != umap.end())
            {
                ans = i + 1;
                break;
            }
            else
            {
                umap[arr[i]]++;
            }
        }
        cout << ans << endl;
    }
}