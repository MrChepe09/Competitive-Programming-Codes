#include <iostream>
using namespace std;

// Structure MinMax
struct Pair
{
    int min;
    int max;
};

// Direct Method
struct Pair directMethod(int n, int arr[])
{
    struct Pair minmax;
    int i;
    if (n % 2 == 0)
    {
        if (arr[0] > arr[1])
        {
            minmax.max = arr[0];
            minmax.min = arr[1];
        }
        else
        {
            minmax.min = arr[0];
            minmax.max = arr[1];
        }
        i = 2;
    }
    else
    {
        minmax.min = arr[0];
        minmax.max = arr[0];
        i = 1;
    }

    while (i < n - 1)
    {
        if (arr[i] > arr[i + 1])
        {
            if (arr[i] > minmax.max)
            {
                minmax.max = arr[i];
            }
            if (arr[i + 1] < minmax.min)
            {
                minmax.min = arr[i + 1];
            }
        }
        else
        {
            if (arr[i + 1] > minmax.max)
            {
                minmax.max = arr[i + 1];
            }
            if (arr[i] < minmax.min)
            {
                minmax.min = arr[i];
            }
        }
        i += 2;
    }
    return minmax;
};

struct Pair tournamentMethod(int n, int arr[], int low, int high)
{
    struct Pair minimax, mm1, mm2;
    minimax.max = arr[low];
    minimax.min = arr[low];

    if (low == high)
    {
        return minimax;
    }
    else if (low == high - 1)
    {
        minimax.max = max(minimax.max, max(arr[low], arr[high]));
        minimax.min = min(minimax.min, min(arr[low], arr[high]));
        return minimax;
    }
    else
    {
        int mid = (low + high) / 2;
        mm1 = tournamentMethod(n, arr, low, mid);
        mm2 = tournamentMethod(n, arr, mid + 1, high);
        if (mm1.min < mm2.min)
            minimax.min = mm1.min;
        else
            minimax.min = mm2.min;

        if (mm1.max > mm2.max)
            minimax.max = mm1.max;
        else
            minimax.max = mm2.max;
        return minimax;
    }
}

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    // Pair minimax = directMethod(n, arr);
    Pair minimax = tournamentMethod(n, arr, 0, n - 1);

    cout << "Maximum is: " << minimax.max << '\n';
    cout << "Minimum is: " << minimax.min;
};