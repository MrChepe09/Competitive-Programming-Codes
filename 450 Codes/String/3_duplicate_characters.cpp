#include <iostream>
#include <string>
#include <map>
using namespace std;

void duplicateChar(string str)
{
    map<char, int> mp;
    for (int i = 0; i < str.length(); i++)
    {
        mp[str[i]]++;
    }
    for (auto it : mp)
    {
        if (it.second > 1)
        {
            cout << it.first << " ";
        }
    }
    cout << endl;
}

int main()
{
    string str;
    cin >> str;
    duplicateChar(str);
}