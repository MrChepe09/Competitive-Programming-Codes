// Problem Link:- https://codeforces.com/contest/617/problem/A

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int count = 0;
    while (n != 0)
    {
        if (n >= 5)
        {
            n -= 5;
        }
        else if (n >= 4)
        {
            n -= 4;
        }
        else if (n >= 3)
        {
            n -= 3;
        }
        else if (n >= 2)
        {
            n -= 2;
        }
        else if (n >= 1)
        {
            n -= 1;
        }
        count++;
    }
    // int size = 1000001;
    // vector<int> arr(size, 0);
    // arr[0] = 0;
    // arr[1] = 1;
    // arr[2] = 1;
    // arr[3] = 1;
    // arr[4] = 1;
    // arr[5] = 1;
    // cout << "hh" << arr[5] << endl;
    // for (int i = 6; i < size; i++)
    // {
    //     arr[i] = min(arr[i - 1], min(arr[i - 2], min(arr[i - 3], min(arr[i - 4], arr[i - 5])))) + 1;
    // }
    // int n;
    // cin >> n;
    cout << count;
}