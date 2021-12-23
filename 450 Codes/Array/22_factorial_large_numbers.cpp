#include <iostream>
using namespace std;

int multiply(int x, int res[], int res_size)
{
    int carry = 0, i = 0;
    while (i < res_size)
    {
        int prod = (res[i] * x) + carry;
        res[i] = prod % 10;
        carry = prod / 10;
        i++;
    }

    while (carry)
    {
        res[res_size] = carry % 10;
        carry = carry / 10;
        res_size++;
    }
    return res_size;
}

void factorial(int n)
{
    int res[500];
    res[0] = 1;
    int res_size = 1;

    int x = 2;
    while (x <= n)
    {
        res_size = multiply(x, res, res_size);
        x += 1;
    }
    cout << "The factorial of " << n << " is: ";
    for (int i = res_size - 1; i >= 0; i--)
    {
        cout << res[i];
    }
}

int main()
{
    int n;
    cin >> n;
    factorial(n);
}