#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
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

        map<int, int> umap;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            umap[arr[i]]++;
        }

        int mini = 1;
        int space = 0;

        for (auto it : umap)
        {
            int count = it.second;
            int rem = mini * it.first - space;

            if (count > rem)
            {
                mini += ceil(((count - rem) / (float)it.first));
            }

            space += count;
        }
        cout << mini << endl;
    }
}