#include <iostream>
using namespace std;

void sortarray(int arr1[], int arr2[], int m, int n)
{
    for (int i = n - 1; i >= 0; i--)
    {
        int last = arr1[m - 1];
        int j = m - 2;
        while (j >= 0 && arr1[j] > arr2[i])
        {
            arr1[j + 1] = arr1[j];
            j--;
        }
        if (j != m - 2 || last > arr2[i])
        {
            arr1[j + 1] = arr2[i];
            arr2[i] = last;
        }
    }
}

// 1 3 5 7 8
// 2 4 6 9

int main()
{
    int n, m;
    cin >> m >> n;
    int arr1[m], arr2[n];
    for (int i = 0; i < m; i++)
    {
        cin >> arr1[i];
    }
    for (int i = 0; i < n; i++)
    {
        cin >> arr2[i];
    }
    sortarray(arr1, arr2, m, n);
    cout << "First array: ";
    for (int i = 0; i < m; i++)
    {
        cout << arr1[i] << " ";
    }
    cout << '\n';
    cout << "Second array: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr2[i] << " ";
    }
}