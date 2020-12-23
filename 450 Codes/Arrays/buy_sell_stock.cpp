#include <iostream>
using namespace std;

int stock(int n, int arr[])
{
    int mini = INT16_MAX;
    int maxi = 0;
    for (int i = 0; i < n; i++)
    {
        mini = min(mini, arr[i]);
        maxi = max(maxi, arr[i] - mini);
    }
    return maxi;
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
    int profit = stock(n, arr);
    cout << "Max Profit is: " << profit;
}