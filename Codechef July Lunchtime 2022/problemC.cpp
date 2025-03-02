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
        vector<int> boys(n), girls(n);
        for (int i = 0; i < n; i++)
            cin >> boys[i];
        for (int i = 0; i < n; i++)
            cin >> girls[i];
        sort(boys.begin(), boys.end());
        sort(girls.begin(), girls.end());
        vector<int> ans;
        for (int i = n / 2, j = 0; i < n; i++, j++)
        {
            ans.push_back(boys[i] + girls[n - 1 - j]);
        }
        sort(ans.begin(), ans.end());
        cout << ans[0] << endl;
    }
}