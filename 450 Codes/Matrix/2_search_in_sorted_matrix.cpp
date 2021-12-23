#include <iostream>
#include <vector>
using namespace std;

void search_element(int n, int m, vector<vector<int>> arr, int find)
{
    int smallest = arr[0][0];
    int largest = arr[n - 1][m - 1];
    if (find < smallest || find > largest)
    {
        cout << "Rlement not in matrix" << endl;
        return;
    }
    int i = 0;
    int j = m - 1;
    while (i < n && j >= 0)
    {
        if (arr[i][j] == find)
        {
            cout << "Element found at Row " << i << " and Column " << j << endl;
            return;
        }
        if (arr[i][j] > find)
        {
            j--;
        }
        else
        {
            i++;
        }
    }
    cout << "Element not found" << endl;
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
    int find;
    cin >> find;
    search_element(n, m, arr, find);
}