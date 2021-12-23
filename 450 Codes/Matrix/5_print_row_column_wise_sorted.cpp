#include <iostream>
#include <vector>
using namespace std;

void young_tableau(int i, int j, int n, int m, vector<vector<int>> &arr)
{
    int down = i + 1 < n ? arr[i + 1][j] : INT16_MAX;
    int right = j + 1 < m ? arr[i][j + 1] : INT16_MAX;

    if (down == INT16_MAX && right == INT16_MAX)
    {
        return;
    }

    if (down < right)
    {
        arr[i][j] = down;
        arr[i + 1][j] = INT16_MAX;
        young_tableau(i + 1, j, n, m, arr);
    }
    else
    {
        arr[i][j] = right;
        arr[i][j + 1] = INT16_MAX;
        young_tableau(i, j + 1, n, m, arr);
    }
}

int extract_min(int n, int m, vector<vector<int>> &arr)
{
    int ret = arr[0][0];
    arr[0][0] = INT16_MAX;
    young_tableau(0, 0, n, m, arr);
    return ret;
}

// Young's tableau
void print_sorted(int n, int m, vector<vector<int>> arr)
{
    for (int i = 0; i < (n * m); i++)
    {
        cout << extract_min(n, m, arr) << " ";
    }
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
    print_sorted(n, m, arr);
}