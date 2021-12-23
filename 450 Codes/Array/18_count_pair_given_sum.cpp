#include <iostream>
#include <unordered_map>
using namespace std;

int countpairs(int n, int arr[], int k)
{
    unordered_map<int, int> m;

    for (int i = 0; i < n; i++)
    {
        m[arr[i]]++;
    }

    int twice = 0;

    for (int i = 0; i < n; i++)
    {
        twice += m[k - arr[i]];

        if (k - arr[i] == arr[i])
        {
            twice--;
        }
    }
    return twice / 2;
}

int main()
{
    int n, k;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cin >> k;
    int count = countpairs(n, arr, k);
    cout << "Total pairs are: " << count;
}