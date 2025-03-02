#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int main()
{
    int test;
    while (test--)
    {
        int n;
        cin >> n;
        string a, b;
        cin >> a;
        cin >> b;
        int cnt = 0;
        unordered_set<char> uset;
        for (int i = 0; i < n; i++)
        {
            if (a[i] != b[i])
            {
                if (uset.find(b[i]) == uset.end())
                {
                    cnt++;
                    uset.insert(b[i]);
                }
            }
        }
        cout << cnt << endl;
    }
}