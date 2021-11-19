// Sort array of 0, 1 and 2 in O(n)
// Set low on 0-index as end of 0's
// Set mid on 0-index as iterator
// Set high on (n-1)-index as start of 2's

// P.S mid iterator is not increased when we found 2 since it is changed
// with high and we don't know what high is.
#include <iostream>
using namespace std;

void sort012(int n, int arr[])
{
    int low = 0;
    int mid = 0;
    int high = n - 1;
    while (mid <= high)
    {
        if (arr[mid] == 0)
        {
            int temp = arr[mid];
            arr[mid] = arr[low];
            arr[low] = temp;
            low++;
            mid++;
        }
        else if (arr[mid] == 1)
        {
            mid++;
        }
        else
        {
            int temp = arr[mid];
            arr[mid] = arr[high];
            arr[high] = temp;
            high--;
        }
    }
}

void printArray(int arr[])
{
    int n = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
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
    sort012(n, arr);
    cout << "Array after sorting is: ";
    printArray(arr);
}