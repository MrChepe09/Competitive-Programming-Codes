#include <iostream>
using namespace std;

void xorgame(int n, int x, int arr[])
{
    int mat[n][33], res[n];
    for (int i = 0; i < n; i++)
    {
        res[i] = arr[i];
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 33; j++)
        {
            mat[i][j] = 0;
        }
    }
    for (int i = 0; i < n; i++)
    {
        int tem = res[i];
        int j = 0;
        while (tem > 0)
        {
            mat[i][j++] = tem % 2;
            tem /= 2;
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 32; j >= 0; j--)
        {
            if (x > 0 && mat[i][j] == 1)
            {
                int col = 0;
                for (int k = i + 1; k < n - 1; k++)
                {
                    if (mat[k][j] == 1)
                    {
                        col = 1;
                        mat[k][j] = 0;
                        mat[i][j] = 0;
                        x -= 1;
                        break;
                    }
                }
                if (col == 0 && x > 0 && i != n - 1)
                {
                    mat[i][j] = 0;
                    mat[n - 1][j] ^= 1;
                    x -= 1;
                }
            }
        }
    }
    // for (int i = 0; i < n; i++)
    // {
    //     cout << res[i] << " ";
    // }
    // cout << '\n';
    for (int i = 0; i < n; i++)
    {
        int ans = 0;
        for (int j = 0; j < 33; j++)
        {
            // cout << mat[i][j] << " ";
            ans += mat[i][j] * (1 << j);
        }
        res[i] = ans;
    }
    // for (int i = 0; i < n; i++)
    // {
    //     cout << res[i] << " ";
    // }
    // cout << '\n';
    if (x > 0)
    {
        if (x % 2 == 1)
        {
            if (n == 2)
            {
                res[n - 1] ^= 1;
                res[n - 2] ^= 1;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << res[i] << " ";
    }
    cout << '\n';
}

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n, x;
        cin >> n >> x;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        xorgame(n, x, arr);
    }
}