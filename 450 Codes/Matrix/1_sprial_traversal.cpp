#include <iostream>
#include <vector>
using namespace std;

void spiral_traversal(int n, int m, vector<vector<int>> arr)
{
    int top = 0, down = n - 1;
    int left = 0, right = m - 1;
    int dir = 0;
    while (top <= down && left <= right)
    {
        if (dir == 0)
        {
            for (int i = left; i <= right; i++)
            {
                cout << arr[top][i] << " ";
            }
            top++;
        }

        if (dir == 1)
        {
            for (int i = top; i <= down; i++)
            {
                cout << arr[i][right] << " ";
            }
            right--;
        }

        if (dir == 2)
        {
            for (int i = right; i >= left; i--)
            {
                cout << arr[down][i] << " ";
            }
            down--;
        }

        if (dir == 3)
        {
            for (int i = down; i >= top; i--)
            {
                cout << arr[i][left] << " ";
            }
            left++;
        }
        dir = (dir + 1) % 4;
    }
    cout << endl;
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
    spiral_traversal(n, m, arr);
}