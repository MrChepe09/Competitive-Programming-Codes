#include <iostream>
#include <string>
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
        string s;
        cin >> s;
        vector<char> vowels{'a', 'e', 'i', 'o', 'u'};
        int maxi = 0;
        int curr = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (find(vowels.begin(), vowels.end(), s[i]) == vowels.end())
            {
                curr++;
            }
            else
            {
                maxi = max(maxi, curr);
                curr = 0;
            }
        }
        maxi = max(maxi, curr);
        if (maxi < 4)
        {
            // cout << maxi << endl;
            cout << "YES" << endl;
        }
        else
        {
            // cout << maxi << endl;
            cout << "NO" << endl;
        }
    }
}