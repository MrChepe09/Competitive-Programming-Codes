#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void values(int x, int y)
{
    vector<int> ans1{2, x ^ 2, x ^ y ^ 2}, ans2{x ^ 2, 2, y ^ 2}, ans3{x ^ y ^ 2, y ^ 2, 2};
    int count = 0;
    for (int i = 0; i < 3; i++)
    {
        if (ans1[i] % 2 == 0)
        {
            count++;
        }
    }
    if (count == 1)
    {
        sort(ans1.begin(), ans1.end());
        cout << ans1[0] << " " << ans1[1] << " " << ans1[2] << endl;
        return;
    }
    count = 0;
    for (int i = 0; i < 3; i++)
    {
        if (ans2[i] % 2 == 0)
        {
            count++;
        }
    }
    if (count == 1)
    {
        sort(ans2.begin(), ans2.end());
        cout << ans2[0] << " " << ans2[1] << " " << ans2[2] << endl;
        return;
    }
    count = 0;
    for (int i = 0; i < 3; i++)
    {
        if (ans3[i] % 2 == 0)
        {
            count++;
        }
    }
    if (count == 1)
    {
        sort(ans3.begin(), ans3.end());
        cout << ans3[0] << " " << ans3[1] << " " << ans3[2] << endl;
        return;
    }
}

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int x, y;
        cin >> x >> y;
        values(x, y);
    }
}