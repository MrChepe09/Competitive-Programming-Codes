#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int max_histogram(int n, vector<int> arr)
{
    stack<int> s;

    int max_area = 0;
    int top;
    int area_top;
    int i = 0;

    while (i < n)
    {
        if (s.empty() || arr[s.top()] <= arr[i])
        {
            s.push(i++);
        }
        else
        {
            top = s.top();
            s.pop();

            area_top = arr[top] * (s.empty() ? i : i - s.top() - 1);

            if (max_area < area_top)
            {
                max_area = area_top;
            }
        }
    }

    while (s.empty() == false)
    {
        top = s.top();
        s.pop();
        area_top = arr[top] * (s.empty() ? i : i - s.top() - 1);

        if (max_area < area_top)
            max_area = area_top;
    }

    return max_area;
}

int max_rectangle(int n, int m, vector<vector<int>> arr)
{
    int res = max_histogram(m, arr[0]);

    for (int i = 1; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {

            if (arr[i][j])
            {
                arr[i][j] += arr[i - 1][j];
            }
        }
        res = max(res, max_histogram(m, arr[i]));
    }
    return res;
}

int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<int>> arr(n);
    for (int i = 0; i < n; i++)
    {
        arr[i] = vector<int>(m);
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
        }
    }
    cout << max_rectangle(n, m, arr);
}