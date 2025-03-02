#include <iostream>
#include <string>
using namespace std;

bool copypush(int n, string s)
{
    if (n == 1)
    {
        return true;
    }
    string s1, s2;
    if (n % 2 == 0)
    {
        s1 = s.substr(0, n / 2);
        s2 = s.substr(n / 2, n / 2);
        if (s1 != s2)
        {
            return false;
        }
        else
        {
            return copypush(n / 2, s1);
        }
    }
    else
    {
        s1 = s.substr(0, n - 1);
        return copypush(n - 1, s1);
    }
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

        bool ans = copypush(n, s);
        if (ans)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}