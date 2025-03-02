#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string longestSubSeq(string &s1, string &s2)
{
    int m = s1.length();
    int n = s2.length();

    int dp[m + 1][n + 1];

    for (int i = 0; i <= m; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if (s1[i - 1] == s2[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    int index = dp[m][n];

    string ans(index + 1, '\0');

    int i = m, j = n;
    while (i > 0 && j > 0)
    {
        if (s1[i - 1] == s2[j - 1])
        {
            ans[index - 1] = s1[i - 1];
            i--;
            j--;
            index--;
        }
        else if (dp[i - 1][j] > dp[i][j - 1])
            i--;
        else
            j--;
    }

    return ans;
}
string longest_pallindrome(string str)
{
    string revStr = str;
    reverse(revStr.begin(), revStr.end());

    return longestSubSeq(str, revStr);
}

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        cout << longest_pallindrome(s) << endl;
    }
}