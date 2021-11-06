#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr[n][n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> arr[i][j];
        }
    }
    int find;
    cin >> find;
    int s1 = 0, s2 = n - 1;
    while (s1 != n || s2 != -1)
    {
        if (arr[s1][s2] == find)
        {
            cout << "Yes";
            break;
        }
        else if (arr[s1][s2] < find)
        {
            if (s1 == n - 1)
            {
                cout << "No";
                break;
            }
            s1 += 1;
        }
        else
        {
            if (s2 == 0)
            {
                cout << "No";
                break;
            }
            s2 -= 1;
        }
    }
}