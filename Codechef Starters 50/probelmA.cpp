#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n, x;
        cin >> n >> x;
        int maxGreatest = x - n + 1;
        if (x < n || x > n * n)
        {
            cout << -1 << endl;
        }
        else
        {
            cout << maxGreatest << " ";
            for (int i = 1; i <= n; i++)
            {
                if (i != maxGreatest)
                    cout << i << " ";
            }
            cout << endl;
        }
    }
}