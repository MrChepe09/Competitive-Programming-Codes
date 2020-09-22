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
#define LOOPX   for(ll i=0;i<n;i++){if(max==a[i])max_value++;}
#define SS second
#define loop1 for(ll i=0;i<k;i++){ans=(ans%MOD*(n-i)%MOD)%MOD;ans=div1(ans,i+1);}
#define ll long long int
#define MOD 1000000007
#define clr(val) memset(val,0,sizeof(val))
#define what_is(x) cerr << #x << " is " << x << endl; 
#define MAXLOOP  for(ll i=0;i<n;i++){if(max<a[i])max=a[i];}
#define OJ \
    freopen("input.txt", "r", stdin); \
    freopen("output.txt", "w", stdout);
#define speed ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
 



ll powerLL(ll x, ll n) 
{ 
    ll result = 1; 
    while (n) { 
        if (n & 1) 
            result = result * x % MOD; 
        n = n / 2; 
        x = x * x % MOD; 
    } 
    return result; 
} 

ll min(ll a,ll b)
{
    return a<b?a:b;

}


ll div1(ll a,ll b)
{
    return (a%MOD *(powerLL(b,MOD-2)%MOD))%MOD;
}


ll sol1(ll n, ll r)
{
    ll ans=1;
    ll k=min(r,n-r);
    
    loop1

    return ans%MOD;
}


void solve()
{
    ll n;
    cin>>n;
    ll a[n],ans;

    for(ll i=0;i<n;i++)
    {
        cin>>a[i];
    }


    
    ll max=0,max_value=0;
    
    
   MAXLOOP
    
  LOOPX


    if(n==1){
        cout<<2;
        return;}


     if(max_value%2!=0)
        ans=powerLL(2,n)%MOD;

     else
     {
         ans=powerLL(2,n)%MOD-((powerLL(2,n-max_value)%MOD)*sol1(max_value,max_value/2)%MOD)%MOD;

     }

     if(ans<0)
        ans=(ans+MOD)%MOD;

     cout<<ans%MOD;
        
}

int main() 
{
 
 speed

 int t;
 cin>>t;

 while(t--)
 {
     solve();
     cout<<"\n";
 }
 
 
 
return 0;
   
}