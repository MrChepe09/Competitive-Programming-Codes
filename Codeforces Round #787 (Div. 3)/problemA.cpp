#include <iostream>
#include <vector>
using namespace std;

bool problem(int a, int b, int c, int x, int y)
{
    c -= (max(0, (x - a)));
    c -= (max(0, (y - b)));
    if (c >= 0)
    {
        // cout << c << endl;
        return true;
    }
    // cout << c << endl;
    return false;
}

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int a, b, c, x, y;
        cin >> a >> b >> c >> x >> y;
        cout << (problem(a, b, c, x, y) ? "YES" : "NO") << endl;
    }
}