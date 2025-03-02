#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n, h, m;
        cin >> n >> h >> m;
        int minHr = 24, minMin = 60;
        for (int i = 0; i < n; i++)
        {
            int ah, am;
            cin >> ah >> am;
            int currHr, currMin;
            if (ah == h)
            {
                if (am < m)
                {
                    currHr = 23;
                    currMin = (60 + am) - m;
                }
                else
                {
                    currHr = 0;
                    currMin = am - m;
                }
            }
            else if (ah > h)
            {
                if (am < m)
                {
                    currHr = ah - h - 1;
                    currMin = (60 + am) - m;
                }
                else
                {
                    currHr = ah - h;
                    currMin = am - m;
                }
            }
            else
            {
                if (am < m)
                {
                    currHr = (24 + ah) - h - 1;
                    currMin = (60 + am) - m;
                }
                else
                {
                    currHr = (24 + ah) - h;
                    currMin = am - m;
                }
            }
            if (currHr < minHr || (currHr == minHr && currMin < minMin))
            {
                minHr = currHr;
                minMin = currMin;
            }
            // cout << currHr << " " << currMin << " " << minHr << " " << minMin << endl;
        }
        cout << minHr << " " << minMin << endl;
    }
}