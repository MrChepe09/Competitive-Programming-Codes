#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int sortmethod(int n, int arr[])
{
    sort(arr, arr + n);
    for (int i = 1; i < n; i++)
    {
        if (arr[i] == arr[i - 1])
        {
            return arr[i];
        }
    }
}

int setmethod(int n, int arr[])
{
    set<int> seen;
    for (int i = 0; i < n; i++)
    {
        if (seen.find(arr[i]) != seen.end())
        {
            return arr[i];
        }
        seen.insert(arr[i]);
    }
}

int floydcycle(int n, int arr[])
{
    int first = arr[0];
    int second = arr[0];
    while (true)
    {
        first = arr[first];
        second = arr[arr[second]];
        if (first == second)
        {
            break;
        }
    }
    first = arr[0];
    while (first != second)
    {
        first = arr[first];
        second = arr[second];
    }
    return second;
}

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    // int ans = sortmethod(n, arr);
    // int ans = setmethod(n, arr);
    int ans = floydcycle(n, arr);
    cout << "The duplicate element is: " << ans;
}