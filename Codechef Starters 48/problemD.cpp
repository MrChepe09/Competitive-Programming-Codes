#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int test;
    cin >> test;
    while (test--)
    {
        int n, k;
        cin >> n >> k;
        vector<int> parent(n);
        parent[0] = -1;
        for (int i = 1; i < n; i++)
            cin >> parent[i];

        
    }
}