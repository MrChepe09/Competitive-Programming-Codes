#include<bits/stdc++.h>
using namespace std;
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL);
#define pb push_back
#define mp make_pair
#define wr(i) cout<<#i<<" = "<<i<<",  ";
#define wre(i) cout<<#i<<"  =  "<<i<<endl;
#define all(v) v.begin(),v.end()
typedef long long ll;
#define lim 1000000000000000LL
typedef unsigned long long ull;
#define M 200005LL
#define F first
#define S second
using u64= uint64_t;

ll func(ll n){
    return (n*(n+1))/2;
}

int main()
{
fast
ll t=1LL;
cin>>t;

while(t--)
{
ll n;
cin>>n;
ll sum=(n*(n+1))/2;
ll ans1=0;
if(sum&1)ans1=0;
else{
    double tmp=sum/2;

    double k=(sqrt(8*tmp+1)/2)-0.5;
    // k=k-0.00000000001;
    double deci,inti;
    deci=modf(k,&inti);
	//cout<<deci<<" "<<inti;
    ll ans=(ll)k;
    if(deci==0){
        ans1=func(ans-1)+func(n-ans-1);
		cout<<ans1<<"hh";
        // wr(func(ans-1))wr(func(n-ans-1))
    }
    // wr(ans)
    ans1+=n-ans;
}
cout<<ans1<<"\n";


}
} 