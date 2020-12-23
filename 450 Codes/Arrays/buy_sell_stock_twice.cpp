#include <iostream>
using namespace std;

int profit(int n, int arr[])
{
    int dp[n];
    for (int i = 0; i < n; i++)
    {
        dp[i] = 0;
    }

    int maxi = arr[n - 1];
    int mini = arr[0];
    for (int i = n - 2; i >= 0; i--)
    {
        if (arr[i] > maxi)
        {
            maxi = arr[i];
        }
        dp[i] = max(dp[i + 1], maxi - arr[i]);
    }

    for (int i = 1; i < n; i++)
    {
        if (arr[i] < mini)
        {
            mini = arr[i];
        }
        dp[i] = max(dp[i - 1], dp[i] + (arr[i] - mini));
    }
    return dp[n - 1];
}

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Maximum profit is: " << profit(n, arr);
}