#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int gcd(int a, int b)
{
    if (a == 0)
        return b;
    if (b == 0)
        return a;

    if (a == b)
        return a;

    if (a > b)
        return gcd(a - b, b);
    return gcd(a, b - a);
}

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n;
        cin >> n;
        vector<int> arr(n);
        vector<int> gaps;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            gaps.push_back(abs(arr[i] - (i + 1)));
        }

        int ans = gaps[0];
        for (int i = 1; i < gaps.size(); i++)
        {
            ans = gcd(ans, gaps[i]);
        }
        cout << ans << endl;
    }
}