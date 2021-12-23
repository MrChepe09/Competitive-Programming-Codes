#include <iostream>
#include <vector>
using namespace std;

int max_row_1(int n, int m, vector<vector<int>> arr)
{
    int max_row = 0;
    int j = m - 1;
    for (int i = 0; i < n; i++)
    {
        bool flag = false;
        while (j >= 0 and arr[i][j] == 1)
        {
            j--;
            flag = true;
        }
        if (flag)
        {
            max_row = i;
        }
    }
    if (max_row == 0 && arr[0][m - 1] == 0)
    {
        return -1;
    }
    return max_row;
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
    cout << max_row_1(n, m, arr);
}