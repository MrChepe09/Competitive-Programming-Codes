#include <iostream>
#include <string>
using namespace std;

string reverse(string str)
{
    int start = 0, end = str.length() - 1;
    while (start < end)
    {
        char temp = (str)[start];
        (str)[start] = (str)[end];
        (str)[end] = temp;
        start++;
        end--;
    }
    return str;
}

int main()
{
    string str;
    cin >> str;
    string ans = reverse(str);
    cout << ans << endl;
}