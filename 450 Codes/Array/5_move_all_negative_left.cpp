// Move all the negative elements to one side of array
// same as sort 0-1-2
// mid as iterator if negative change with low
// if positive increment mid

#include <iostream>
using namespace std;

void negativeLeft(int n, int arr[])
{
    int low = 0;
    int mid = 0;
    while (mid < n)
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