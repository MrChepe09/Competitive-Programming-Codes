#include <iostream>
#include <vector>
#include <set>
using namespace std;
int equivalent(string s, int size, int num1, int num2, vector<int> vec, int sum1, int sum2, int length)
{
    // vector<pair<int, int>> vec_str;
    set<pair<pair<int, int>, pair<int, int>>> str_eq;
    str_eq.insert(make_pair(make_pair(num1, num2), make_pair(sum1, sum2)));
    // for(int i=0; i<vec_str.size(); i++){
    //     cout<<vec_str[i];
    // }
    for (int i = size; i < length; i++)
    {
        if (s[i - size] == '1')
        {
            vec.erase(vec.begin());
            int t = sum2;
            sum2 = sum1;
            sum1 = t;
            num1 -= 1;
        }
        else
        {
            num2 -= 1;
            vec[0] -= 1;
            sum2 -= 1;
        }
        if (s[i] == '1')
        {
            num1 += 1;
            vec.push_back(0);
        }
        else
        {
            num2 += 1;
            vec[vec.size() - 1] += 1;
            if (vec.size() % 2 == 1)
            {
                // for(int i=0; i<vec_str.size(); i++){
                //     cout<<vec_str[i];
                // }
                // cout<<vec[i];
                sum2 += 1;
            }
            else
            {
                // cout<<vec[i];
                sum1 += 1;
            }
        }
        // for(int i=0; i<vec.size(); i++){
        //     cout<<vec[i]<<" "<<'\n';
        // }
        str_eq.insert(make_pair(make_pair(num1, num2), make_pair(sum1, sum2)));
    }
    return str_eq.size();
}
int string_equivalent(string s, int n, int length)
{
    vector<int> vec;
    int rt = 0, num1 = 0, num2 = 0, sum1 = 0, sum2 = 0, cur = 0;
    for (int i = 0; i < n; i++)
    {
        if (s[i] == '0')
        {
            if (cur % 2 == 0)
                sum2 += 1;
            else
                sum1 += 1;
            rt += 1;
            num2 += 1;
        }
        else
        {
            vec.push_back(rt);
            rt = 0;
            cur += 1;
            num1 += 1;
        }
    }
    // for(int i=0; i<vec.size(); i++){
    //     cout<<vec[i]<<" "<<'\n';
    // }
    vec.push_back(rt);
    return equivalent(s, n, num1, num2, vec, sum1, sum2, length);
}

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        string s;
        cin >> s;
        int ans = 0;
        for (int i = 0; i < s.size(); i++)
        {
            ans += string_equivalent(s, i + 1, s.size());
        }
        cout << ans << endl;
    }
}