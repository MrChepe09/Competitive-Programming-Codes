#include <iostream>
#include <vector>
using namespace std;

// FOR EACH CELL GET THE MAX OF THAT ROW AND COLUMN
// AND GET THE DIFFERENCE BETWEEN THE (I, J) AND (I+1, J+1) CELLS
int specific_pair(int n, int m, vector<vector<int>> arr)
{
    int maxValue = INT16_MIN;
    int maxArr[n][m];
    maxArr[n - 1][m - 1] = arr[n - 1][m - 1];

    // PRE PROCESS THE LAST COLUMN
    int maxv = arr[n - 1][m - 1];
    for (int j = m - 2; j >= 0; j--)
    {
        if (arr[n - 1][j] > maxv)
        {
            maxv = arr[n - 1][j];
        }
        maxArr[n - 1][j] = maxv;
    }

    // PRE PROCESS THE LAST ROW
    maxv = arr[n - 1][m - 1];
    for (int i = n - 2; i >= 0; i--)
    {
        if (arr[i][m - 1] > maxv)
        {
            maxv = arr[i][m - 1];
        }
        maxArr[i][m - 1] = maxv;
    }

    // ITERATE OVER MATRIX TO FIND THE MAX PAIR
    for (int i = n - 2; i >= 0; i--)
    {
        for (int j = m - 2; j >= 0; j--)
        {
            if (maxArr[i + 1][j + 1] - arr[i][j] > maxValue)
            {
                maxValue = maxArr[i + 1][j + 1] - arr[i][j];
            }
            maxArr[i][j] = max(arr[i][j], max(maxArr[i + 1][j], maxArr[i][j + 1]));
        }
    }
    return maxValue;
}

int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<int>> arr(n);
    for (int i = 0; i < n; i++)
    {
        arr[i] = vector<int>(m);
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
        }
    }
    cout << specific_pair(n, m, arr);
}