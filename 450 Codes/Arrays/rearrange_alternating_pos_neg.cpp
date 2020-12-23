#include <iostream>
using namespace std;

void rightRotate(int arr[], int n, int out, int ind)
{
    int temp = arr[ind];
    for (int i = ind; i > out; i--)
    {
        arr[i] = arr[i - 1];
    }
    arr[out] = temp;
}

void rearrange(int n, int arr[])
{
    int outPlace = -1;
    for (int i = 0; i < n; i++)
    {
        if (outPlace >= 0)
        {
            if ((arr[i] >= 0 && arr[outPlace] < 0) || (arr[i] < 0 && arr[outPlace] >= 0))
            {
                rightRotate(arr, n, outPlace, i);
                if (i - outPlace >= 2)
                {
                    outPlace += 2;
                }
                else
                {
                    outPlace = -1;
                }
            }
        }
        if (outPlace == -1)
        {
            if ((arr[i] >= 0 && i % 2 == 0) || (arr[i] < 0 && i % 2 != 0))
            {
                outPlace = i;
            }
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
    rearrange(n, arr);
    cout << "The array after rearranging is: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}