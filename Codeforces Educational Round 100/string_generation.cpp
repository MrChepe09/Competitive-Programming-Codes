#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        string s = "";
        for (int i = 0; i < k; i++)
        {
            s += 'a';
        }
        int p = n - k;
        int j = 0;
        int arr[] = {'b', 'c', 'a'};
        for (int i = 0; i < p; i++)
        {
            // cout<<arr[i]%
            s += arr[i % 3];
        }
        cout << s << endl;
    }
}