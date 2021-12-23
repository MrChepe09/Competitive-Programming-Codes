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

int profitAlt(int n, int arr[])
{
    int buy1, profit1, buy2, profit2;
    buy1 = buy2 = INT16_MAX;
    profit1 = profit2 = 0;

    for (int i = 0; i < n; i++)
    {
        buy1 = min(buy1, arr[i]);
        profit1 = max(profit1, arr[i] - buy1);
        buy2 = min(buy2, arr[i] - profit1);
        profit2 = max(profit2, arr[i] - buy2);
    }

    return profit2;
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