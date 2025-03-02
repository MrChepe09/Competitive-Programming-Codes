#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    vector<int> arr(n - 1);
    for (int i = 0; i < n - 1; i++)
        cin >> arr[i];

    int start = 1;

    do
    {
        start = start + arr[start - 1];
        if (start == k)
        {
            cout << "YES" << endl;
            return 0;
        }
    } while (start < n);
    cout << "NO" << endl;
}