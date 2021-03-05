#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, x;
        cin >> n >> x;
        float arr[n];
        float max = 0;
        float min = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            min += arr[i];
            max += (int)ceil(arr[i] / x);
            // cout << "hell" << max << endl;
        }
        min = (int)ceil(min / x);
        cout << (int)min << " " << (int)max << endl;
    }
}