#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

void common_elements(int n, int m, vector<vector<int>> arr)
{
    unordered_map<int, int> umap;
    for (int j = 0; j < m; j++)
    {
        umap[arr[0][j]] = 1;
    }

    for (int i = 1; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (umap[arr[i][j]] == i)
            {
                umap[arr[i][j]] = i + 1;
                if (i == n - 1 && umap[arr[i][j]] == n)
                {
                    cout << arr[i][j] << " ";
                }
            }
        }
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
    common_elements(n, m, arr);
}