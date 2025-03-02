#include <iostream>
// #include <string>
#include <vector>
// #include <algorithm>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        int posOne = -1;
        int posN = -1;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] == 1)
                posOne = i;
            if (arr[i] == n)
                posN = i;
        }
        int oneLeft = posOne;
        int nLeft = (n - 1) - posN;
        if (posOne > posN)
            cout << (oneLeft + nLeft - 1) << endl;
        else
            cout << (oneLeft + nLeft) << endl;
    }
}