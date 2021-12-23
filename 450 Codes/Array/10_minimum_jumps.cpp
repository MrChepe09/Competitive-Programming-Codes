#include <iostream>
using namespace std;

// O(N^N)
int jumps(int n, int arr[])
{
    int jumps[n];
    for (int i = 0; i < n; i++)
    {
        jumps[i] = 0;
    }
    if (n == 0 || arr[0] == 0)
    {
        return -1;
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

// O(N)
int jumps2(int n, int arr[])
{
    if (n <= 1)
    {
        return 0;
    }
    if (arr[0] == 0)
    {
        return -1;
    }

    int maxReach = arr[0];
    int steps = arr[0];
    int jump = 1;
    for (int i = 1; i < n; i++)
    {
        if (i == n - 1)
        {
            return jump;
        }
        steps--;
        maxReach = max(maxReach, arr[i] + i);
        if (steps == 0)
        {
            jump++;
            if (i >= maxReach)
            {
                return -1;
            }
            steps = maxReach - i;
        }
    }
    return -1;
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