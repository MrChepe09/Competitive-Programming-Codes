#include<bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin>>s;
    s += '$';
    int n = s.size();
    vector<int> p(n), c(n);
    {
        // k = 0
        vector<pair<char, int>> a(n);
        for (int i = 0; i<n; i++) a[i] = {s[i], i};
        sort(a.begin(), a.end());

        for(int i=0; i<n; i++) p[i] = a[i].second;
        c[p[0]] = 0;
        for(int i = 1; i<n; i++) {
            if(a[i].first == a[i-1].first) {
                c[p[i]] = c[p[i-1]];
            } else {
                c[p[i]] = c[p[i-1]] + 1;
            }
        }
    }

    int k = 0;
    while((1 << k) < n){
        // k -> k + 1
        vector<pair<pair<int, int>, int>> a(n);
        for (int i=0; i<n; i++){
            a[i] = {{c[i], c[(i+(1<<k)) % n]}, i};
        }
        sort(a.begin(), a.end());
        for(int i=0; i<n; i++) p[i] = a[i].second;
        c[p[0]] = 0;
        for(int i = 1; i<n; i++) {
            if(a[i].first == a[i-1].first) {
                c[p[i]] = c[p[i-1]];
            } else {
                c[p[i]] = c[p[i-1]] + 1;
            }
        }
        k++;
    }

    for(int i=0; i<n; i++){
        cout<<p[i]<<" ";
    }
}