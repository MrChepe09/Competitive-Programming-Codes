#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

bool isSubset(int n, int m, int arr1[], int arr2[])
{
    sort(arr1, arr1 + n);
    sort(arr2, arr2 + m);
    int i = 0, j = 0;
    while (i < n && j < m)
    {
        if (arr1[i] == arr2[j])
        {
            i++;
            j++;
        }
        else if (arr1[i] < arr2[j])
        {
            i++;
        }
        else if (arr1[i] > arr2[j])
        {
            return false;
        }
    }
    return (j < m) ? false : true;
}

bool isSubsetAlt(int n, int m, int arr1[], int arr2[])
{
    set<int> hashset;
    for (int i = 0; i < n; i++)
    {
        hashset.insert(arr1[i]);
    }

    for (int i = 0; i < m; i++)
    {
        if (hashset.find(arr2[i]) == hashset.end())
            return false;
    }
    return true;
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
    if (isSubset(n, m, arr1, arr2))
    {
        cout << "is a subset" << endl;
    }
    else
    {
        cout << "is not a subset" << endl;
    }
}