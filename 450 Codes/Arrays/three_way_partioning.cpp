#include <iostream>
using namespace std;

void partition(int n, int arr[], int a, int b)
{
    int start = 0;
    int mid = 0;
    int end = n - 1;
    while (mid <= end)
    {
        if (arr[mid] < a)
        {
            swap(arr[mid], arr[start]);
            mid++;
            start++;
        }
        else if (arr[mid] > b)
        {
            swap(arr[mid], arr[end]);
            end--;
        }
        else
        {
            mid++;
        }
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
    int a, b;
    cin >> a >> b;
    partition(n, arr, a, b);
    cout << "The array after partitioning is: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}