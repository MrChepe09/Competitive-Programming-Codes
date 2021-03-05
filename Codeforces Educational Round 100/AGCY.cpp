#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, q;
        cin >> n >> q;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            arr[i] = 0;
        }
        for (int i = 0; i < q; i++)
        {
            int l, r;
            cin >> l >> r;
            arr[l - 1]++;
            arr[r - 1]-=r-l+1;
        }
    }
}