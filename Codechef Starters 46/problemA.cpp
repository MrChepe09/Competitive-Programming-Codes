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
        int count = 0;
        bool startCheck = false;
        int i = s.size() - 1;
        while (i >= 0)
        {
            if (s[i] == '0')
            {
                startCheck = true;
            }
            if (startCheck)
            {
                if (s[i] == '1')
                {
                    while (i >= 0 && s[i] == '1')
                    {
                        i--;
                    }
                    count++;
                }
            }
            i--;
        }
        cout << count << endl;
    }
}