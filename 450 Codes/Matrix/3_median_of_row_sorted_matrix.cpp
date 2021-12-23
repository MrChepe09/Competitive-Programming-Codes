#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int median_matrix(int n, int m, vector<vector<int>> arr)
{
    int maxi = INT32_MIN, mini = INT32_MAX;
    for (int i = 0; i < n; i++)
    {
        maxi = max(maxi, arr[i][m - 1]);
        mini = min(mini, arr[i][0]);
    }
    int desired = (n * m + 1) / 2;
    while (mini < maxi)
    {
        int mid = mini + (maxi - mini) / 2;
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            count += upper_bound(arr[i].begin(), arr[i].end(), mid) - arr[i].begin();
        }
        if (count < desired)
        {
            mini = mid + 1;
        }
        else
        {
            maxi = mid;
        }
    }
    return mini;
}

int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<int>> arr(n);
    for (int i = 0; i < n; i++)
    {
        arr[i] = vector<int>(m);
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
        }
    }
    cout << median_matrix(n, m, arr);
}