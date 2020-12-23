#include <iostream>
#include <algorithm>
using namespace std;

int minimize(int n, int arr[], int k)
{
    if (n == 1)
    {
        return 0;
    }
    sort(arr, arr + n);
    int res = arr[n - 1] - arr[0];
    int small = arr[0] + k;
    int big = arr[n - 1] - k;
    if (small > big)
    {
        int temp = small;
        small = big;
        big = temp;
    }
    for (int i = 1; i < n - 1; i++)
    {
        int sub = arr[i] - k;
        int add = arr[i] + k;
        if (sub >= small || add <= big)
        {
            continue;
        }
        if (big - sub <= add - small)
        {
            small = sub;
        }
        else
        {
            big = add;
        }
    }
    return min(res, big - small);
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