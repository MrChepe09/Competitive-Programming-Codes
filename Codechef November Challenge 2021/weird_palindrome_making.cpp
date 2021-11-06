#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int arr[n];
        int odds = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            if (arr[i] % 2 != 0)
            {
                odds++;
            }
        }
        int ans = 0;
        while (odds > 1)
        {
            odds -= 2;
            ans += 1;
        }
        cout << ans << endl;
    }
}