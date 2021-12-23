#include <iostream>
#include <set>
using namespace std;

int subseq(int n, int arr[])
{
    set<int> s;
    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        s.insert(arr[i]);
    }
    for (int i = 0; i < n; i++)
    {
        if (s.find(arr[i] - 1) == s.end())
        {
            int j = arr[i];
            while (s.find(j) != s.end())
            {
                j++;
            }
            cnt = max(cnt, j - arr[i]);
        }
    }
    return cnt;
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
    cout << "The length of longest consecutive subsequence is: " << subseq(n, arr);
}