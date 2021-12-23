#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

struct Interval
{
    int start, end;
};

bool compareInterval(Interval i1, Interval i2)
{
    return (i1.start < i2.start);
}

void mergeIntervals(Interval arr[], int n)
{
    if (n <= 0)
    {
        return;
    }

    stack<Interval> s;
    sort(arr, arr + n, compareInterval);
    s.push(arr[0]);

    for (int i = 1; i < n; i++)
    {
        Interval top = s.top();

        if (top.end < arr[i].start)
        {
            s.push(arr[i]);
        }
        else if (top.end < arr[i].end)
        {
            top.end = arr[i].end;
            s.pop();
            s.push(top);
        }
    }

    cout << "The Merged Intervals are: ";
    while (!s.empty())
    {
        Interval t = s.top();
        cout << "[" << t.start << "," << t.end << "] ";
        s.pop();
    }
    return;
}

int main()
{
    int n;
    cin >> n;
    Interval arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i].start >> arr[i].end;
    }
    mergeIntervals(arr, n);
}