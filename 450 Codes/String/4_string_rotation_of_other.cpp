#include <iostream>
#include <string>
#include <queue>
using namespace std;

// with concatenation
bool rotationCheck(string s1, string s2)
{
    if (s1.length() != s2.length())
    {
        return false;
    }
    string temp = s1 + s1;
    if (temp.find(s2) == string::npos)
    {
        return false;
    }
    return true;
}

// with Queue
bool rotationCheckQueue(string s1, string s2)
{
    if (s1.length() != s2.length())
    {
        return false;
    }
    queue<char> q1;
    for (int i = 0; i < s1.length(); i++)
    {
        q1.push(s1[i]);
    }
    queue<char> q2;
    for (int i = 0; i < s2.length(); i++)
    {
        q2.push(s2[i]);
    }
    int k = s2.length();
    while (k--)
    {
        char temp = q2.front();
        q2.pop();
        q2.push(temp);
        if (q1 == q2)
        {
            return true;
        }
    }
    return false;
}

int main()
{
    string str1, str2;
    cin >> str1 >> str2;
    cout << (rotationCheckQueue(str1, str2) ? "isRotation" : "notARotation") << endl;
}