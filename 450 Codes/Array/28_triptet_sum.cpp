#include <iostream>
#include <algorithm>
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

bool s3sumAlt(int A[], int arr_size, int sum)
{
    int l, r;

    sort(A, A + arr_size);

    for (int i = 0; i < arr_size - 2; i++)
    {
        l = i + 1;
        r = arr_size - 1;
        while (l < r)
        {
            if (A[i] + A[l] + A[r] == sum)
            {
                printf("Triplet is %d, %d, %d", A[i],
                       A[l], A[r]);
                return true;
            }
            else if (A[i] + A[l] + A[r] < sum)
            {
                l++;
            }
            else
            {
                r--;
            }
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