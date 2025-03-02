#include <iostream>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n;
        cin >> n;
        int start;
        if (n % 2 == 1)
        {
            start = n;
        }
        else
        {
            start = n - 1;
        }
        while (start > 0)
        {
            cout << start << " ";
            start -= 2;
        }
        start = 2;
        while (start <= n)
        {
            cout << start << " ";
            start += 2;
        }
        cout << endl;
    }
}
