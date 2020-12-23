#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        int done = 0, rem = n - k;
        int arr[n];

        for (int i = 0; i < n; i++)
        {
            if (n / 2 <= k)
            {
                if ((i + 1) % 2 != 0 && done < rem)
                {
                    arr[i] = -(i + 1);
                    done++;
                }
                else
                {
                    arr[i] = (i + 1);
                }
            }
            else
            {
                if ((i + 1) % 2 == 0 && done < k)
                {
                    arr[i] = (i + 1);
                    done++;
                }
                else
                {
                    arr[i] = -(i + 1);
                }
            }
        }

        for (int i = 0; i < n; i++)
        {
            cout << arr[i] << " ";
        }
        cout << '\n';
    }
}