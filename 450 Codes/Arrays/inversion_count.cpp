#include <iostream>
using namespace std;

int merge(int arr[], int temp[], int low, int mid, int high)
{
    int i = low;
    int j = mid + 1;
    int k = low;
    int count = 0;
    while (i <= mid && j <= high)
    {
        if (arr[i] <= arr[j])
        {
            temp[k] = arr[i];
            k++;
            i++;
        }
        else
        {
            temp[k] = arr[j];
            count += (mid - i + 1);
            k++;
            j++;
        }
    }
    while (i <= mid)
    {
        temp[k] = arr[i];
        k++;
        i++;
    }
    while (j <= high)
    {
        temp[k] = arr[j];
        k++;
        j++;
    }
    for (int loop = low; loop <= high; loop++)
    {
        arr[loop] = temp[loop];
    }
    return count;
}

int mergeSort(int arr[], int temp[], int low, int high)
{
    int inv_count = 0;
    if (low < high)
    {
        int mid = (low + high) / 2;
        inv_count += mergeSort(arr, temp, low, mid);
        inv_count += mergeSort(arr, temp, mid + 1, high);
        inv_count += merge(arr, temp, low, mid, high);
    }
    return inv_count;
}

int inversionCount(int n, int arr[])
{
    int temp[n];
    return mergeSort(arr, temp, 0, n - 1);
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
    int cnt = inversionCount(n, arr);
    cout << "Inversion counts are: " << cnt;
}