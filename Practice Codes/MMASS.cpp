#include<bits/stdc++.h>
using namespace std;

int i = 0;

int molecules(string s){
    vector<int> st;
    while(i<s.size()){
        if(s[i]=='H'){
            st.push_back(1);
            i++;
        } else if (s[i]=='O'){
            st.push_back(16);
            i++;
        } else if (s[i]=='C'){
            st.push_back(12);
            i++;
        } else if(s[i]=='('){
            i++;
            int dd = molecules(s);
            st.push_back(dd);
        } else if (s[i]==')'){
            i++;
            int sum = 0;
            for (int g=0; g<st.size(); g++){
                sum = sum+st[g];
            }
            return sum;
        } else {
            int seti = st.back();
            st.pop_back();
            int di = (int)s[i]-48;
            st.push_back(seti*di);
            i++;
        }
    }
    int sum = 0;
    for (int g=0; g<st.size(); g++){
        sum = sum+st[g];
    }
    return sum;
}

int main(){
    string s;
    cin>>s;
    cout<<molecules(s);
}