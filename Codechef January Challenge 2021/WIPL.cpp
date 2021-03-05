#include <iostream>
using namespace std;

int boxes(int n, int k, int h[])
{
    return 0;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        int height[n];
        for (int i = 0; i < n; i++)
        {
            cin >> height[i];
        }
        cout << boxes(n, k, height) << endl;
    }
}