#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int problem(int n, vector<int> a)
{
    int ans = 0;
    if (n == 2 && a[n - 1] == 0)
    {
        return -1;
    }
    for (int i = n - 2; i >= 0; i--)
    {
        while (a[i] != 0 && a[i] >= a[i + 1])
        {
            a[i] = floor(a[i] / 2);
            ans++;
        }
        if (i != 0 && a[i] == 0)
        {
            return -1;
        }
    }
    return ans;
}

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        int ans = problem(n, a);
        cout << ans << endl;
    }
}