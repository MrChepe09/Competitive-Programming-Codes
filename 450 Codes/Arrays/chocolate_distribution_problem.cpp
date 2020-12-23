#include <iostream>
#include <algorithm>
using namespace std;

int chocolates(int n, int m, int arr[])
{
    if (n == 0 || m == 0)
    {
        return 0;
    }
    sort(arr, arr + n);
    if (n < m)
    {
        return -1;
    }
    int mini = INT32_MAX;
    int i = 0;
    while (i + m - 1 < n)
    {
        int diff = arr[i + m - 1] - arr[i];
        if (diff < mini)
        {
            mini = diff;
        }
        i++;
    }
    return mini;
}

int main()
{
    int n, m;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cin >> m;
    cout << "Minimum difference is: " << chocolates(n, m, arr);
}