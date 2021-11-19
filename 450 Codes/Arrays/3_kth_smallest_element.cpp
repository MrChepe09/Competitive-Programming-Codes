// Find the Kth max and min of an array
// refer QuickSort algorithm
#include <iostream>
using namespace std;

int partition(int arr[], int left, int right)
{
    int x = arr[right];
    int i = left;
    for (int j = left; j < right; j++)
    {
        if (arr[j] <= x)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
        }
    }
    int temp = arr[i];
    arr[i] = arr[right];
    arr[right] = temp;
    return i;
}

int kthelement(int arr[], int left, int right, int k)
{
    int pos = partition(arr, left, right);

    if (pos == k - 1)
    {
        return arr[pos];
    }
    if (pos > k - 1)
    {
        return kthelement(arr, left, pos - 1, k);
    }
    return kthelement(arr, pos + 1, right, k);
    return INT16_MAX;
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
    int res = kthelement(arr, 0, n - 1, k);
    cout << "The kth smallest element is: " << res;
}