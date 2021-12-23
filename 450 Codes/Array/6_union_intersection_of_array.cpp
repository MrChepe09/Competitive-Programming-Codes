// Find the Union and Intersection of an array
// For Union we use a set and insert all elements from
// both the array in it - O(N+M)
// For intersection we use 2-pointer approach - O(max(N, M))

#include <iostream>
#include <set>
using namespace std;

void union_array(int arr1[], int arr2[], int n, int m)
{
    set<int> s;
    for (int i = 0; i < n; i++)
    {
        s.insert(arr1[i]);
    }
    for (int j = 0; j < m; j++)
    {
        s.insert(arr2[j]);
    }
    for (auto it : s)
    {
        cout << it << " ";
    }
    cout << endl;
}

void intersection_array(int arr1[], int arr2[], int n, int m)
{
    int i = 0;
    int j = 0;
    while (i < n and j < m)
    {
        if (arr1[i] == arr2[j])
        {
            cout << arr1[i] << " ";
            i++;
            j++;
        }
        else if (arr1[i] < arr2[j])
        {
            i++;
        }
        else
        {
            j++;
        }
    }
    cout << endl;
}

int main()
{
    int n;
    cin >> n;
    int arr1[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr1[i];
    }
    int m;
    cin >> m;
    int arr2[m];
    for (int i = 0; i < n; i++)
    {
        cin >> arr2[i];
    }
    cout << "Union of both arrays is: ";
    union_array(arr1, arr2, n, m);
    cout << "Intersection of both arrays is: ";
    intersection_array(arr1, arr2, n, m);
}