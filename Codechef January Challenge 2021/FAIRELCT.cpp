#include <iostream>
#include <numeric>
#include <algorithm>
using namespace std;

int election(int n, int m, int a[], int b[])
{
    int a1 = 0, b1 = 0;
    a1 = accumulate(a, a + n, a1);
    b1 = accumulate(b, b + m, b1);
    if (a1 > b1)
    {
        return 0;
    }
    sort(a, a + n);
    sort(b, b + m);
    int count = 0;
    int i = 0;
    int j = m - 1;
    while (a1 <= b1)
    {
        if (i == n || j == -1)
        {
            return -1;
        }
        a1 += b[j];
        b1 -= b[j];
        b1 += a[i];
        a1 -= a[i];
        i++;
        j--;
        count++;
    }
    return count;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        int a[n], b[m];
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        for (int i = 0; i < m; i++)
        {
            cin >> b[i];
        }
        cout << election(n, m, a, b) << endl;
    }
}