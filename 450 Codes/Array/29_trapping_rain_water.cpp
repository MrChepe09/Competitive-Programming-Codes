#include <iostream>
using namespace std;

int trapwater(int n, int arr[])
{
    int left = 0;
    int right = 0;
    int low = 0;
    int high = n - 1;
    int res = 0;
    while (low <= high)
    {
        if (arr[low] < arr[high])
        {
            if (left > arr[low])
            {
                res += (left - arr[low]);
            }
            else
            {
                left = arr[low];
            }
            low++;
        }
        else
        {
            if (right > arr[high])
            {
                res += (right - arr[high]);
            }
            else
            {
                right = arr[high];
            }
            high--;
        }
    }
    return res;
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
    cout << "We can trap " << trapwater(n, arr) << " units of water";
}