#include <iostream>
#include <string>
using namespace std;

string problem(int n, int k, string s)
{
    char charMax = 'a';
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] > charMax)
        {
            if (s[i] - 'a' > k)
            {
            }
        }
    }
    return s;
}

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n, k;
        cin >> n >> k;
        string s;
        cin >> s;
        string ans = problem(n, k, s);
        cout << ans << endl;
    }
}