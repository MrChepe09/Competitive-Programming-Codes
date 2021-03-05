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
    long long ori = 0;
    for (long long i = 1; i <= n; i++)
    {
        ori += i;
    }
    cout << ori - curr;
}