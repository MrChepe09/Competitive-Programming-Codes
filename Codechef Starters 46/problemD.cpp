#include <iostream>
#include <vector>
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
        int begin = 0, end = s.size() - 1;
        bool start = false;
        vector<char> ans(s.size());
        for (int i = s.size() - 1; i >= 0; i--)
        {
            if (start)
            {
                ans[begin++] = s[i];
            }
            else
            {
                ans[end--] = s[i];
            }

            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
            {
                start = !start;
            }
        }

        for (char t : ans)
        {
            cout << t;
        }
        cout << endl;
    }
}
