#include <iostream>
using namespace std;

void swap(int arr[], int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void reverse(int arr[], int n, int i)
{
    int start = i;
    int end = n - 1;
    while (start < end)
    {
        swap(arr, start, end);
        start++;
        end--;
    }
}

void next_permutation(int arr[], int n)
{
    if (n <= 1)
    {
        return;
    }
    // find the index(i) which is smaller than the index(i+1)
    int i = n - 2;
    while (i >= 0 && arr[i] >= arr[i + 1])
    {
        i--;
    }
    if (i >= 0)
    {
        // find the index(j) which is greater than index(i)
        int j = n - 1;
        while (arr[j] <= arr[i])
        {
            j--;
        }

        // swap index(i) and index(j)
        swap(arr, i, j);
    }
    // reverse the array
    reverse(arr, n, i + 1);
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
    next_permutation(arr, n);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}