#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        int arr[n];
        for (int i = 1; i <= n; i++)
        {
            arr[i - 1] = i;
        }
        if (m <= n - 1)
        {
            int i = 0;
            while (m--)
            {
                cout << arr[i] << " " << arr[i + 1] << endl;
                i++;
            }
        }
        else
        {
            int i = 0;
            while (i < n - 1)
            {
                cout << arr[i] << " " << arr[i + 1] << endl;
                i++;
                m--;
            }
            for (int j = 2; j < n; j++)
            {
                if (m == 0)
                {
                    break;
                }
                for (int k = 0; k <= j; k++)
                {
                    if (m == 0)
                    {
                        break;
                    }
                    if (j - 1 != k)
                    {
                        cout << arr[k] << " " << arr[j] << endl;
                        m--;
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }
    }
}