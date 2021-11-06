#include <iostream>
#include <vector>
using namespace std;

int main()
{
    long long n;
    cin >> n;
    long long arr[n];
    long long curr = 0;
    for (long long i = 0; i < n - 1; i++)
    {
        cin >> arr[i];
        curr += arr[i];
    }
    long long original = 0;
    for (long long i = 1; i <= n; i++)
    {
        original += i;
    }
    cout << original - curr;
}

1 + 2 + 3 + 4 + 5 = 15 2 + 3 + 1 + 5 = 11 15 - 11 = 4
