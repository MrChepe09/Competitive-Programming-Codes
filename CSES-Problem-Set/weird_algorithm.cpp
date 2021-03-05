#include <iostream>
#include <vector>
using namespace std;

int main()
{
    long long n;
    cin >> n;
    vector<long long> arr;
    arr.push_back(n);
    while (n != 1)
    {
        if (n % 2 == 1)
        {
            n = (n * 3) + 1;
        }
        else
        {
            n = n / 2;
        }
        arr.push_back(n);
    }
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }
}