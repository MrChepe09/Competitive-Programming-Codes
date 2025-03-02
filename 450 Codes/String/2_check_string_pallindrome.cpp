#include <iostream>
#include <string>
using namespace std;

bool isPallindrome(string str)
{
    int start = 0, end = str.length() - 1;
    while (start < end)
    {
        if (str[start] != str[end])
        {
            return false;
        }
        start++;
        end--;
    }
    return true;
}

int main()
{
    string str;
    cin >> str;
    cout << (isPallindrome(str) ? "Pallindrome" : "not Pallindrome") << endl;
}
