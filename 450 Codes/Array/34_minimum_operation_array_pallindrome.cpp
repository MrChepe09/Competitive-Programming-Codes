#include <iostream>
using namespace std;

int min_operations(int n, int arr[])
{
    int ans = 0;
    int i = 0, j = n - 1;
    while (i < j)
    {
        if (arr[i] == arr[j])
        {
            i += 1;
            j -= 1;
        }
        else if (arr[i] > arr[j])
        {
            j -= 1;
            ans += 1;
            arr[j] += arr[j + 1];
        }
        else
        {
            i += 1;
            ans += 1;
            arr[i] += arr[i - 1];
        }
    }
    return ans;
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
    cout << min_operations(n, arr) << endl;
}