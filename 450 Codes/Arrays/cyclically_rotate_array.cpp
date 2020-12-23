#include <iostream>
using namespace std;

void rotateone(int n, int arr[])
{
    int last = arr[n - 1];
    int high = n - 1;
    while (high > 0)
    {
        arr[high] = arr[high - 1];
        high--;
    }
    arr[0] = last;
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
    rotateone(n, arr);
    cout << "Array after one cyclically rotation: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}