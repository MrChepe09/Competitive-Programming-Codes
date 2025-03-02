#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        sort(arr.begin(), arr.end());
        int cnt = 0;
        int pop = n - 1;
        for (int i = 0; i < n; i++)
        {
            // cout << arr[i] << n << endl;
            if (arr[i] <= pop)
            {
                cnt++;
                pop -= arr[i];
            }
        }
        cout << cnt << endl;
    }
}