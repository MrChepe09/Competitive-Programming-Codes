#include <iostream>
using namespace std;

int swaps(int n, int arr[], int k)
{
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] <= k)
        {
            count++;
        }
    }
    int bad = 0;
    for (int i = 0; i < count; i++)
    {
        if (arr[i] > k)
        {
            bad++;
        }
    }
    int ans = bad;
    for (int i = 0, j = count; j < n; ++i, ++j)
    {
        if (arr[i] > k)
        {
            bad--;
        }
        if (arr[j] > k)
        {
            bad++;
        }
        ans = min(ans, bad);
    }
    return ans;
}

int main()
{
    int n, k;
    cin >> n >> k;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Minimum swaps to get k elements together: " << swaps(n, arr, k);
}