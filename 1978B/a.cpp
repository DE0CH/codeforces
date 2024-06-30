
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

ll solve(ll n, ll a, ll b) {
    if (b <= a) {
        return n * a;
    
    } else if (n <= b - a - 1) {
        return n * (b + b - n + 1) / 2;
    } else if (n >= b - a) {
        ll ee = (b-a) * (b-a + 1) / 2;
        ll gg = n*a;
        return ee + gg;
    } else {
        throw runtime_error("unreachable");
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int tc = 1;
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        ll a, b, n;
        cin >> n >> a >> b;
        cout << solve(n, a, b) << endl;
    }
}