#include <iostream>
using namespace std;

void negativeLeft(int n, int arr[])
{
    int low = 0;
    int mid = 0;
    int high = n - 1;
    while (mid <= high)
    {
        if (arr[mid] < 0)
        {
            int temp = arr[low];
            arr[low] = arr[mid];
            arr[mid] = temp;
            low++;
            mid++;
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
    negativeLeft(n, arr);
    cout << "Array after moving is: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}