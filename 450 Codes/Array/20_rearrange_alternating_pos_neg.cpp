#include <iostream>
using namespace std;

void swap(int arr[], int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void rearrange(int n, int arr[])
{
    int i = 0, j = n - 1;
    while (i < j)
    {
        while (i <= n - 1 && arr[i] > 0)
        {
            i += 1;
        }
        while (j >= 0 and arr[j] < 0)
        {
            j -= 1;
        }
        if (i < j)
        {
            swap(arr, i, j);
        }
    }
    if (i == 0 || i == n)
    {
        return;
    }
    int k = 0;
    while (k < n && i < n)
    {
        swap(arr, k, i);
        i++;
        k += 2;
    }
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
    rearrange(n, arr);
    cout << "The array after rearranging is: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}