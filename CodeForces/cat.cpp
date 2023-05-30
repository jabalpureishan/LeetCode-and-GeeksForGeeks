#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define MOD 1000000007
#define SIZE 1e6+2
#define endl "\n"


void solve() {
    ll n; cin>>n;
    string s; cin>>s;
    ll m=0,e=0,o=0,w=0;
    ll ind=0;
    if(s[ind]=='m' or s[ind]=='M')
    while((s[ind]=='m' or s[ind]=='M') and ind<n){
        m=1;
        ind++;
    }
    else{
        cout<<"NO"<<endl;
        return;
    }
    if(s[ind]=='e' or s[ind]=='E')
    while((s[ind]=='e' or s[ind]=='E') and ind<n){
        e=1;
        ind++;
    }
    else{
        cout<<"NO"<<endl;
        return;
    }
    if(s[ind]=='o' or s[ind]=='O')
    while((s[ind]=='o' or s[ind]=='O') and ind<n){
        o=1;
        ind++;
    }
    else{
        cout<<"NO"<<endl;
        return;
    }
    if(s[ind]=='w' or s[ind]=='W')
    while((s[ind]=='w' or s[ind]=='W') and ind<n){
        w=1;
        ind++;
    }
    else{
        cout<<"NO"<<endl;
        return;
    }
    
    if(m==1 and e==1 and o==1 and e==1 and ind==n) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
    
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    ll t; cin>>t;
    while(t--){
        solve();
    }
    return 0;
}