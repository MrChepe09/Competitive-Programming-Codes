#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void print_matrix(int n, int m, vector<vector<int>> arr)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

// rotating my cycles for each frames of rows and columns
// first frame is of first row - last row - first col - last col
void rotate_matrix(int n, int m, vector<vector<int>> arr)
{
    for (int i = 0; i < n / 2; i++)
    {
        for (int j = i; j < n - i - 1; j++)
        {
            int temp = arr[i][j];
            arr[i][j] = arr[j][n - 1 - i];
            arr[j][n - 1 - i] = arr[n - 1 - i][n - 1 - j];
            arr[n - 1 - i][n - 1 - j] = arr[n - 1 - j][i];
            arr[n - 1 - j][i] = temp;
        }
    }
    print_matrix(n, m, arr);
}

// for anticlock-wise rotate -> reverse row -> transpose
// for clock-wise rotate -> transpose -> reverse column
void rotate_by_transpose(int n, int m, vector<vector<int>> arr)
{
    // reverse row
    for (int i = 0; i < n; i++)
    {
        reverse(arr[i].begin(), arr[i].end());
    }

    // transpose
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            swap(arr[i][j], arr[j][i]);
        }
    }
    print_matrix(n, m, arr);
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
    rotate_by_transpose(n, m, arr);
}