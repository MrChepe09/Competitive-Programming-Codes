#include <iostream>
#include <string>
using namespace std;

string countAndSay(int n)
{
    if (n == 1)
        return "1";
    else if (n == 2)
        return "11";
    string res = "11";
    for (int i = 3; i <= n; i++)
    {
        res += "$";
        string temp = "";
        int cnt = 1;
        for (int j = 1; j < res.length(); j++)
        {
            if (res[j] != res[j - 1])
            {
                temp += cnt + '0';
                temp += res[j - 1];
                cnt = 1;
            }
            else
            {
                cnt++;
            }
        }
        res = temp;
    }
    return res;
}

int main()
{
    int n;
    cin >> n;
    cout << countAndSay(n) << endl;
}
