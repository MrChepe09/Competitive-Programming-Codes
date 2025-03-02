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
        string a, b;
        cin >> a;
        cin >> b;
        string zero_one = "", one_zero = "";
        for (int i = 0; i < n; i++)
        {
            if (i & 1)
            {
                one_zero += '1', zero_one += '0';
            }
            else
            {
                one_zero += '0', zero_one += '1';
            }
        }
        int one = count(a.begin(), a.end(), '1');

        if (one)
        {
            if (b == one_zero || b == zero_one)
            {
                if (a == b)
                {
                    cout << "YES" << endl;
                }
                else
                {
                    cout << "NO" << endl;
                }
            }
            else
            {
                cout << "YES" << endl;
            }
        }
        else
        {
            if (a == b)
            {
                cout << "YES" << endl;
            }
            else
            {
                cout << "NO" << endl;
            }
        }
    }
}