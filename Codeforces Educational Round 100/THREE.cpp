#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        int two = 0, one = 0;
        int count = 0;
        unordered_map<char, int> uord;
        for (int i = 0; i < s.size(); i++)
        {
            uord[s[i]]++;
        }
        for (auto x : uord)
        {
            if (x.second % 2 == 0)
            {
                two += x.second / 2;
            }
            else
            {
                one++;
                two += x.second / 2;
            }
        }
        while (one < two)
        {
            two--;
            one += 2;
        }
        cout << two << endl;
    }
}