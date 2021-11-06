#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int trig = 0;
        int n;
        cin >> n;
        int arr[n];
        unordered_map<int, int> umap;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            umap[arr[i]]++;
        }
        vector<int> vec;
        for (auto x : umap)
        {
            if (x.second > 2)
            {
                trig = -1;
                break;
            }
            else if (x.second == 2)
            {
                vec.push_back(x.first);
            }
        }
        if (trig == -1)
        {
            cout << -1 << endl;
        }
        else if (umap[*max_element(arr, arr + n)] == 2)
        {
            cout << -1 << endl;
        }
        else
        {
            sort(vec.begin(), vec.end());
            for (int i = 0; i < vec.size(); i++)
            {
                cout << vec[i] << " ";
            }
            sort(arr, arr + n, greater<int>());
            for (int i = 0; i < n; i++)
            {
                if (i == 0)
                {
                    cout << arr[i];
                }
                if (i != 0 && arr[i] != arr[i - 1])
                {
                    cout << " " << arr[i];
                }
            }
            cout << endl;
        }
    }
}