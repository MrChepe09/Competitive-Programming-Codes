#include <iostream>
#include <algorithm>
using namespace std;

int minimize(int n, int arr[], int k)
{
    sort(arr, arr + n);
    int res = arr[n - 1] - arr[0];
    int maxi, mini;
    for (int i = 1; i <= n - 1; i++)
    {
        if (arr[i] >= k) // if towers can't be -ve (remove if condition if allowed)
        {
            maxi = max(arr[n - 1] - k, arr[i - 1] + k);
            mini = min(arr[0] + k, arr[i] - k);
            res = min(res, maxi - mini);
        }
    }
    return res;
}

int main()
{
    int n, k;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cin >> k;
    int diff = minimize(n, arr, k);
    cout << "The minimum height difference is: " << diff;
}