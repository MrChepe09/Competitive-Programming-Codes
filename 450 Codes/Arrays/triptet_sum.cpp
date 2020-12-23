#include <iostream>
#include <set>
using namespace std;

bool s3sum(int n, int arr[], int sum)
{
    for (int i = 0; i < n - 1; i++)
    {
        set<int> s;
        int curr = sum - arr[i];
        for (int j = i + 1; j < n; j++)
        {
            if (s.find(curr - arr[j]) != s.end())
            {
                return true;
            }
            s.insert(arr[j]);
        }
    }
    return false;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, s;
        cin >> n >> s;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        cout << s3sum(n, arr, s) << endl;
    }
}