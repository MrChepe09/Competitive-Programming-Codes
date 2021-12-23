#include <iostream>
using namespace std;

// Time - O(n) || Space - O(1)
int median_by_counting(int n, int arr1[], int arr2[])
{
    int i = 0;
    int j = 0;
    int count;
    int m1 = -1, m2 = -1;
    for (count = 0; count <= n; count++)
    {
        if (i == n)
        {
            m1 = m2;
            m2 = arr2[0];
            break;
        }
        else if (j == n)
        {
            m1 = m2;
            m2 = arr1[0];
            break;
        }
        if (arr1[i] <= arr2[j])
        {
            m1 = m2;
            m2 = arr1[i];
            i++;
        }
        else
        {
            m1 = m2;
            m2 = arr2[j];
            j++;
        }
    }

    return (m1 + m2) / 2;
}

int median(int arr[], int s, int e)
{
    return (arr[(s + e) / 2] + arr[(s + e + 1) / 2]) / 2;
}

// Time - O(logN) || Space - O(1)
int median_by_recursion(int a[], int b[], int Sa, int Sb, int Ea, int Eb)
{
    if (Ea - Sa <= 1)
        return (max(a[Sa], b[Sb]) + min(a[Ea], b[Eb])) / 2;
    int m1 = median(a, Sa, Ea);
    int m2 = median(b, Sb, Eb);
    if (m1 == m2)
        return m1;
    if (m1 > m2)
        return median_by_recursion(a, b, Sa, (Sb + Eb + 1) / 2, (Sa + Ea + 1) / 2, Eb);
    return median_by_recursion(a, b, (Sa + Ea + 1) / 2, Sb, Ea, (Sb + Eb + 1) / 2);
}

int main()
{
    int n;
    cin >> n;
    int arr1[n], arr2[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr1[i];
    }
    for (int i = 0; i < n; i++)
    {
        cin >> arr2[i];
    }
    cout << median_by_counting(n, arr1, arr2) << endl;
    cout << median_by_recursion(arr1, arr2, 0, 0, n - 1, n - 1) << endl;
}