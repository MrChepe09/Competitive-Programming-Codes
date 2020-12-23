#include <iostream>
using namespace std;

long long product(int n, long long arr[])
{
    long long mini = arr[0];
    long long maxi = arr[0];
    long long res = arr[0];
    for (int i = 1; i < n; i++)
    {
        if (arr[i] < 0)
        {
            swap(mini, maxi);
        }
        maxi = max(arr[i], maxi * arr[i]);
        mini = min(arr[i], mini * arr[i]);
        res = max(res, maxi);
    }
    return res;
}

int main()
{
    int n;
    cin >> n;
    long long arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Max Product is: " << product(n, arr);
}