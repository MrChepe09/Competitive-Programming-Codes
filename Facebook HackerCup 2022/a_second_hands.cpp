#include <iostream>
#include <fstream>
#include <unordered_map>
using namespace std;

const string kInputFilename = "second_hands_input.txt";
const string kOutputFilename = "output.txt";

ifstream fin(kInputFilename);
ofstream fout(kOutputFilename);

int main()
{
    int test;
    fin >> test;
    int i = 1;
    while (i <= test)
    {
        int n, k;
        fin >> n >> k;
        unordered_map<int, int> umap;
        for (int i = 0; i < n; i++)
        {
            int a;
            fin >> a;
            umap[a]++;
        }
        bool possible = true;
        for (auto it : umap)
        {
            if (it.second > 2)
                possible = false;
        }
        fout << "Case #" << i++ << ": ";
        if (possible)
        {
            int each = (n + 1) / 2;
            if (each <= k)
                fout << "YES";
            else
                fout << "NO";
        }
        else
        {

            fout << "NO";
        }
        fout << endl;
    }
    fin.close();
    fout.close();
}