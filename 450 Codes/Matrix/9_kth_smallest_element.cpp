#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct HeapNode
{
    int value;
    int row;
    int col;
};

void minHeapify(HeapNode harr[], int i, int size)
{
    int left = i * 2 + 1;
    int right = i * 2 + 2;
    if (left < size && right < size && harr[left].value < harr[i].value && harr[right].value < harr[i].value)
    {
        HeapNode temp = harr[right];
        harr[right] = harr[i];
        harr[i] = harr[left];
        harr[left] = temp;
        minHeapify(harr, left, size);
        minHeapify(harr, right, size);
    }
    if (left < size && harr[left].value < harr[i].value)
    {
        HeapNode temp = harr[i];
        harr[i] = harr[left];
        harr[left] = temp;
        minHeapify(harr, left, size);
    }
}

// Using Heap
int kthsmallest(int n, int m, vector<vector<int>> arr, int k)
{
    if (k < 0 && k >= n * m)
    {
        return INT16_MAX;
    }

    HeapNode harr[n];
    for (int i = 0; i < m; i++)
    {
        harr[i] = {arr[0][i], 0, i};
    }

    HeapNode hr;
    for (int i = 0; i < k; i++)
    {
        hr = harr[0];

        int nextVal = (hr.row < (n - 1)) ? arr[hr.row + 1][hr.col] : INT16_MAX;
        harr[0] = {nextVal,
                   (hr.row) + 1,
                   hr.col};
        minHeapify(harr, 0, n);
    }
    return hr.value;
}

int getElementsGreaterOrEqual(int mid, int n, int m, vector<vector<int>> arr)
{
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i][0] > mid)
        {
            return ans;
        }

        if (arr[i][m - 1] <= mid)
        {
            ans += m;
            continue;
        }

        int greater = 0;
        for (int jump = n / 2; jump >= 1; jump /= 2)
        {
            while (greater + jump < n && arr[i][greater + jump] <= mid)
            {
                greater += jump;
            }
        }

        ans += greater + 1;
    }
    return ans;
}

// By Binary Search
int kthsmallest_bs(int n, int m, vector<vector<int>> arr, int k)
{
    int left = arr[0][0];
    int right = arr[n - 1][m - 1];

    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        int greaterOrMid = getElementsGreaterOrEqual(mid, n, m, arr);

        if (greaterOrMid >= k)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return left;
}

int main()
{
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<int>> arr(n);
    for (int i = 0; i < n; i++)
    {
        arr[i] = vector<int>(m);
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
        }
    }
    cout << kthsmallest_bs(n, m, arr, k);
}