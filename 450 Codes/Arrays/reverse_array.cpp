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

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << "Array before Reversing: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << '\n';
    cout << "Array after Reversing: ";
    reverse(n, arr);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}