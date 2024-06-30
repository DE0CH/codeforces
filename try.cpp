#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

template<
    typename T_container, 
    typename T = typename enable_if<
        !is_same<T_container, string>::value, typename T_container::value_type
    >::type
>
ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }


vector<ll>& make_vector() {
    vector<ll> v = {1, 2, 3, 4};
    return v;
}

int main() {
    vector<ll> v = {1, 2, 3, 4};
    cout << v << endl;
    vector<ll> k = make_vector();
    cout << k << endl;
}