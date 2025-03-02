#include <iostream>
#include <string>
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
        int currMax = 9;
        string ans = "";
        while (n != 0 || currMax > 0)
        {
            if (n >= currMax)
            {
                ans += to_string(currMax);
                n -= currMax;
                currMax--;
            }
            else
            {
                currMax--;
            }
        }
        reverse(ans.begin(), ans.end());
        cout << ans << endl;
    }
}