#include <iostream>
using namespace std;

int gcd(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    return gcd(b, a % b);
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        int arr[m];
        for (int i = 0; i < m; i++)
        {
            cin >> arr[i];
        }
        int abc = arr[0];
        for (int i = 1; i < m; i++)
        {
            abc = gcd(abc, arr[i]);
        }
        if (n >= abc)
        {
            cout << (n - abc) << endl;
        }
        else if (abc == 1)
        {
            cout << (n - 1) << endl;
        }
        else
        {
            int p = n;
            while (p != 0 && abc % p != 0)
            {
                p--;
            }
            cout << n - p << endl;
        }
    }
}