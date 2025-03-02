#include <iostream>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int maxT, maxN, sumN;
        cin >> maxT >> maxN >> sumN;

        if (maxN >= sumN)
        {
            cout << sumN * sumN << endl;
            continue;
        }
        int ans = 0;
        while (sumN > 0 && maxT > 0)
        {
            if (maxN < sumN)
            {
                ans += (maxN * maxN);
                sumN -= maxN;
            }
            else
            {
                ans += (sumN * sumN);
                sumN -= sumN;
            }
            maxT--;
        }
        cout << ans << endl;
    }
}