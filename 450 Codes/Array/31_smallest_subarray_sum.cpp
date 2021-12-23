#include <iostream>
using namespace std;

int subarray(int n, int arr[], int x)
{
    int curr = 0;
    int mini = n + 1;
    int start = 0, end = 0;
    while (end < n)
    {
        while (curr <= x && end < n)
        {
            curr += arr[end];
            end++;
        }
        while (curr > x && start < n)
        {
            if (end - start < mini)
            {
                mini = end - start;
            }
            curr -= arr[start];
            start++;
        }
    }
    return mini;
}

int main()
{
    int n, x;
    cin >> n >> x;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Minimum Length subarray: " << subarray(n, arr, x);
}