#include <iostream>

using namespace std;
int main()
{
    int n, t;
    cin>>t;
    while (t--){
      long long int n, a[100000];
      cin>>n;
      for (int i=0; i<n; i++){
          cin>>a[i];
      }
      long long int c = 0;
      for (long long int j=0; j<n; j++){
          int long long p = 1;
          for(long long int k=j; k<n; k++){
              p = p * a[k];
              if((abs(p%4))!=2){
                  c++;
              }
          }
      }
    cout<<c<<endl;
    }
    return 0;
}
