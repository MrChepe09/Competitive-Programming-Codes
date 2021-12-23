#include <iostream>
using namespace std;

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

// Time - O(logN) || Space - O(1)
int median_binary_search(int n, int m, int arr1[], int arr2[])
{
    if (n > m)
    {
        return median_binary_search(m, n, arr2, arr1);
    }
    int start = 0, end = n - 1;
    int realMid = (n + m + 1) / 2;
    while (start <= end)
    {
        int mid = (start + end) / 2;
        int leftASize = mid;
        int leftBSize = realMid - leftASize;
        int leftA = (leftASize > 0) ? arr1[leftASize - 1] : INT16_MIN;
        int leftB = (leftBSize > 0) ? arr2[leftBSize - 1] : INT16_MIN;
        int rightA = (leftASize < n) ? arr1[leftASize] : INT16_MAX;
        int rightB = (leftBSize < m) ? arr2[leftBSize] : INT16_MAX;

        if (leftA <= rightB && leftB <= rightA)
        {
            if ((n + m) % 2 == 0)
            {
                return (max(leftA, leftB) + min(rightA, rightB)) / 2;
            }
            else
            {
                return max(leftA, leftB);
            }
        }
        else if (leftA > rightB)
        {
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }
    return 0;
}

int main()
{
    int n, m;
    cin >> n >> m;
    int arr1[n], arr2[m];
    for (int i = 0; i < n; i++)
    {
        cin >> arr1[i];
    }
    for (int i = 0; i < m; i++)
    {
        cin >> arr2[i];
    }
    cout << median_binary_search(n, m, arr1, arr2) << endl;
    cout << median_by_recursion(arr1, arr2, 0, 0, n - 1, m - 1) << endl;
}