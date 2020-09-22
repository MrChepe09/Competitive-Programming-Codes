#include<bits/stdc++.h>
using namespace std;
 
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define endl "\n"
#define sd(val) scanf("%d",&val)
#define ss(val) scanf("%s",&val)
#define sl(val) scanf("%lld",&val)
#define debug(val) printf("check%d\n",val)
#define all(v) v.begin(),v.end()
#define PB push_back
#define MP make_pair
#define FF first
#define arr_ip for(int i=0;i<n;i++){cin>>a[i]}
#define arr_op for(int i=0;i<n;i++) {cout<<a[i]}
#define SS second
#define ll long long int
#define loop1 for(ll i=1;i<=20;i++){cout<<1<<" "<<(1ul<<i)<<endl;cout.flush();cin>>x;xorvalue.push_back(x);};
#define loop2 for(ll i=1;i<xorvalue.size();i++){if(xorvalue[i]>=sum){xorvalue[i]=((n-(xorvalue[i]-sum)/(1ul<<(xorvalue.size()-i)))/2);}else{xorvalue[i]=(n+(sum-xorvalue[i])/(1ul<<(xorvalue.size()-i)))/2;}};



#define MOD 1000000007
#define clr(val) memset(val,0,sizeof(val))
#define what_is(x) cerr << #x << " is " << x << endl; 
#define OJ \
    freopen("input.txt", "r", stdin); \
    freopen("output.txt", "w", stdout);
#define speed ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
 


int subtask()
{
    ll n,ans=0;

    cin>>n;


    vector<ll>xorvalue;

    ll x;

    loop1


    reverse(xorvalue.begin(),xorvalue.end());


    ll sum=xorvalue[0]-n*(1ul<<20);

    loop2

    for(int i=1;i<xorvalue.size();i++)
     {if(xorvalue[i]%2!=0)
        ans+=1ul<<(xorvalue.size()-i);}

    if(sum%2!=0)
        ans++;
    cout<<2<<" "<<ans<<endl;
    cout.flush();

    int res;
    cin>>res;

    return res;
     
} 
 
int main() 
{
 
 speed

 int t;
 cin>>t;

 while(t--)
 {
     if(!subtask())
        break;
    

    cout<<endl;
    cout.flush();
 }
 
 
 
return 0;
   
}