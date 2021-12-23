// Kadane's algorithm to find largest sum contiguous subarray
// At each index starting from 1 save the max_till_this_index and
// max_overall. Lastly return the max_overall
// P.S: We will not store negatives in max_till_this_index and replace it with 0

#include <iostream>
using namespace std;

int kadane(int n, int arr[])
{
    int curr_max = arr[0];
    int max_so = arr[0];
    for (int i = 1; i < n; i++)
    {
        curr_max = curr_max + arr[i];
        max_so = max(max_so, curr_max);
        if (curr_max < 0)
        {
            curr_max = 0;
        }
    }
    return max_so;
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
    int res = kadane(n, arr);
    cout << "Maximum sum contigous sub-array is: " << res;
}