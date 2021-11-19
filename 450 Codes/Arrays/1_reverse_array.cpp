// Reversing an array
// Set a pointer on start and one at end
// exchange the data between low and high variables
// keep on increasing the start and decreasing the end
// until the end is greater than start.
#include <iostream>
using namespace std;

void reverse(int n, int arr[])
{
    int low = 0;
    int high = n - 1;

    while (low < high)
    {
        int temp = arr[low];
        arr[low] = arr[high];
        arr[high] = temp;
        low++;
        high--;
    }
}

void printArray(int arr[])
{
    int n = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
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
    reverse(n, arr);
    printArray(arr);
}