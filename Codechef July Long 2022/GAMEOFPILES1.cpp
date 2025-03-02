#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n;
        cin >> n;
        vector<int> arr(n);
        int sum = 0;
        bool isOne = false;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            sum += (arr[i] - 2);
            if (arr[i] == 1)
                isOne = true;
        }
        if (isOne)
        {
            cout << "CHEF" << endl;
            continue;
        }
        else
        {
            if (sum % 2 == 0)
                cout << "CHEFINA" << endl;
            else
                cout << "CHEF" << endl;
        }
    }
}