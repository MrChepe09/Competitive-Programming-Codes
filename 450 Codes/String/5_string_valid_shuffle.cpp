#include <iostream>
#include <string>
#include <map>
using namespace std;

// if we can shuffle the string order
bool validShuffle(string s1, string s2, string s3)
{
    if (s1.length() + s2.length() != s3.length())
    {
        return false;
    }
    map<char, int> m1;
    for (int i = 0; i < s1.length(); i++)
    {
        m1[s1[i]]++;
    }
    for (int i = 0; i < s2.length(); i++)
    {
        m1[s2[i]]++;
    }
    map<char, int> m2;
    for (int i = 0; i < s3.length(); i++)
    {
        m2[s3[i]]++;
    }
    for (auto it : m1)
    {
        if (m2[it.first] != it.second)
        {
            return false;
        }
    }
    return true;
}

// if we cannot shuffle the strings order
bool validShuffle2(string s1, string s2, string s3)
{
    int n = s1.length(), m = s2.length(), res = s3.length();
    if (n + m != res)
    {
        return false;
    }
    int i = 0, j = 0, k = 0;
    while (k < res)
    {
        if (i < n && s1[i] == s3[k])
        {
            i++;
        }
        else if (j < m && s2[j] == s3[k])
        {
            j++;
        }
        k++;
    }
    if (i == n && j == m)
    {
        return true;
    }
    return false;
}

int main()
{
    string str1, str2, str3;
    cin >> str1 >> str2 >> str3;
    cout << (validShuffle2(str1, str2, str3) ? "isAValidShuffle" : "isNotAValidShuffle") << endl;
}