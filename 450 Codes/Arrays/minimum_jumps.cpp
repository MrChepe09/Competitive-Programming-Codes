#include <iostream>
using namespace std;

int jumps(int n, int arr[])
{
    int jumps[n];
    for (int i = 0; i < n; i++)
    {
        jumps[i] = 0;
    }
    if (n == 0 || arr[0] == 0)
    {
        return INT32_MAX;
    }
    for (int i = 1; i < n; i++)
    {
        jumps[i] = INT32_MAX;
        for (int j = 0; j < i; j++)
        {
            if (i <= j + arr[j] && jumps[j] != INT32_MAX)
            {
                jumps[i] = min(jumps[i], jumps[j] + 1);
                break;
            }
        }
    }
    return jumps[n - 1];
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
    int res = jumps(n, arr);
    cout << "The minimum no. of jumps required: " << res;
}