#include <iostream>
#include <set>
using namespace std;

bool subarray(int n, int arr[])
{
    set<int> s;
    int sumi = 0;
    for (int i = 0; i < n; i++)
    {
        sumi += arr[i];
        if (sumi == 0 || (s.find(sumi) != s.end()))
        {
            return true;
        }
        s.insert(arr[i]);
    }
    return false;
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
    if (subarray(n, arr))
    {
        cout << "There is a subarray with sum 0";
    }
    else
    {
        cout << "There is no subarray";
    }
}