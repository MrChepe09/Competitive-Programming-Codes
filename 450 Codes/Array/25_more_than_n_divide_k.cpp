#include <iostream>
using namespace std;

struct eleCount
{
    int e;
    int c;
};

void moreThanNdK(int n, int arr[], int k)
{
    if (k < 2)
    {
        return;
    }

    struct eleCount temp[k - 1];
    for (int i = 0; i < k - 1; i++)
    {
        temp[i].c = 0;
        // cout << "ele " << temp[i].e << endl;
    }

    for (int i = 0; i < n; i++)
    {
        int j;
        for (j = 0; j < k - 1; j++)
        {
            if (temp[j].e == arr[i])
            {
                temp[j].c++;
                break;
            }
        }
        //cout << j << "Hello ";
        if (j == k - 1)
        {
            int l;
            for (l = 0; l < k - 1; l++)
            {
                if (temp[l].c == 0)
                {
                    temp[l].e = arr[i];
                    temp[l].c = 1;
                    //cout << "ele: " << temp[i].e;
                    break;
                }
            }

            if (l == k - 1)
            {
                for (l = 0; l < k - 1; l++)
                {
                    temp[l].c--;
                }
            }
        }
    }

    for (int i = 0; i < k - 1; i++)
    {
        int ac = 0;
        for (int j = 0; j < n; j++)
        {
            if (arr[j] == temp[i].e)
            {
                ac++;
            }
            //cout << ac;
        }
        if (ac > n / k)
        {
            cout << "Number: " << temp[i].e << " Count: " << ac << endl;
        }
    }
}

int main()
{
    int n, k;
    cin >> n >> k;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    moreThanNdK(n, arr, k);
}