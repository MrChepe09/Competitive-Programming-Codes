#include<bits/stdc++.h>
#define     ll          long long int
#define     ld          double
#define     REP(i,x,n)    for(ll i=x;i<n;i++)
#define     SZ(v)       (ll)v.size()
#define     endl        "\n"
#define     ff          first
#define     ss          second
#define     PQ_MIN      priority_queue <ll, vector<ll>, greater<ll> >
#define     PQ          priority_queue <int>
#define     pbds        tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
#define     setbit(x)   __builtin_popcount(x)
#define     prec(n)     fixed<<setprecision(n)
#define     pb(n)       push_back(n)
#define     mp(a,b)     make_pair(a,b)
#define     clr(n)      memset(n,0,sizeof(n))
#define     reset(n)    memset(n,-1,sizeof(n))
#define     ii          pair<ll,ll>
#define     vll         vector<ll>
#define     PI          3.1415926535897932384626433832795028841971693993751

using namespace std;
void solve(){

ll a,target;
cin>>a>>target;
ll n=a,t=target;
map<ll,ll> ma;

for(ll i=2;i*i<=a;i++)
{
    if(a%i==0)
    {
        ll cnt=0;

        while(a%i==0)
        {
            a/=i;
            cnt++;
        }
        ma[i]=cnt;
    }
}
if(a>1)
{
    ma[a]=1;

}

map<ll,ll> mt;
for(ll i=2;i*i<=target;i++)
{
    if(target%i==0)
    {
        ll cnt=0;

        while(target%i==0)
        {
            target/=i;
            cnt++;
        }
        mt[i]=cnt;
    }
}
if(target>1)
{
    mt[target]=1;
}


ll ans=0;
for(map<ll,ll>::iterator it=ma.begin();it!=ma.end();it++)
{
    while(t%n!=0 && it->ss>0)
    {
        it->ss--;
        n/=it->ff;
        ans++;
    }
    if(t%n==0)
    {
        break;
    }
}

for(map<ll,ll>::iterator it=mt.begin();it!=mt.end();it++)
{
    while(t!=n && it->ss>0)
    {
        ans++;
        n*=it->ff;
        it->ss--;
    }
    if(t==n)
    {
        break;

    }

}
cout<<ans;

}
int main(){
//    freopen("timber_input", "r", stdin);
//    freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	ll t=1;
//	cin>>t;
    REP(i,1,t+1)
    {
//    cout<<"Case #"<<i<<": ";
		solve();
    }
	return 0;
}
