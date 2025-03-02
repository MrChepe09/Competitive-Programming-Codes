#include <iostream>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int curr = x1 + y1;
        int dest = x2 + y2;
        if (curr % 2 == 1 && dest % 2 == 1)
        {
            cout << "YES" << endl;
        }
        else if (curr % 2 == 0 && dest % 2 == 0)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
}