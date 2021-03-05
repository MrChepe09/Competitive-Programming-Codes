#include <iostream>
using namespace std;

int sumele(int n, int x, int arr[])
{
    int ans = 0;
    int flag = 0;
    int i = 0;
    int h = x;
    while (arr[i] % x == 0)
    {
        if (flag == 0)
        {
            ans += arr[i];
        }
        else
        {
            ans += (arr[i]) * h;
        }
        arr[i] /= x;
        i++;
        if (i == n)
        {
            flag = 1;
            i = 0;
            h *= x;
        }
        cout << ans << "hh" << endl;
    }
    for (int j = i; j < n; j++)
    {
        ans += arr[j];
    }
    return ans;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, x;
        cin >> n >> x;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        cout << sumele(n, x, arr) << endl;
    }
}