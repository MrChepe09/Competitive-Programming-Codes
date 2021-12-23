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

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << max_histogram(n, arr);
}