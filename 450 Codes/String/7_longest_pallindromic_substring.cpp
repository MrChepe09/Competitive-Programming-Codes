#include <iostream>
#include <string>
#include <cstring>
using namespace std;

// Using 2-pointers
int longPal2(string s)
{
    int n = s.size();
    if (n < 2)
    {
        return n;
    }

    int maxLength = 1, start = 0;
    int low, high;
    for (int i = 1; i < n - 1; i++)
    {
        low = i - 1;
        high = i + 1;
        while (low >= 0 && high < n && s[low] == s[high])
        {
            low--;
            high++;
        }
        low++;
        high--;
        if (high - low + 1 > maxLength)
        {
            start = low;
            maxLength = high - low + 1;
        }
        low = i;
        high = i + 1;
        while (low >= 0 && high < n && s[low] == s[high])
        {
            low--;
            high++;
        }
        low++;
        high--;
        if (high - low + 1 > maxLength)
        {
            start = low;
            maxLength = high - low + 1;
        }
    }
    return maxLength;
}

// Using DP
int longPal(string s)
{
    int n = s.size();
    bool table[n][n];
    memset(table, 0, sizeof(table));

    int maxLength = 1;

    for (int i = 0; i < n; i++)
    {
        table[i][i] = true;
    }

    int start = 0;
    for (int i = 0; i < n - 1; i++)
    {
        if (s[i] == s[i + 1])
        {
            table[i][i + 1] = true;
            start = i;
            maxLength = 2;
        }
    }

    for (int k = 3; k <= n; k++)
    {
        for (int i = 0; i < n - k + 1; i++)
        {
            int j = i + k - 1;

            if (table[i + 1][j - 1] && s[i] == s[j])
            {
                table[i][j] = true;

                if (k > maxLength)
                {
                    start = i;
                    maxLength = k;
                }
            }
        }
    }
    return maxLength;
}

int main()
{
    string s;
    cin >> s;
    cout << longPal2(s) << endl;
}