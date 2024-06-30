#include <bits/stdc++.h>

using namespace std;

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ","; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

ll find(vector<ll> *things, ll start, ll l, ll r) {
    ll end = start;
    ll sum = 0;
    while (!((l <= sum) && (sum <= r))) {
        if (sum < l && end < things->size()) {
            sum += things->at(end);
            end++;
        } else if (sum > r && start < end) {
            sum -= things->at(start);
            start++;
        } else {
            dbg(start, end, sum);
            break;
        }
    } 
    if ((l <= sum) && (sum <= r)) {
        return end;
    } else {
        return -1;
    }
}

vector<ll> things;

ll solve(vector<ll> *things, ll l, ll r) {
    ll start = 0;
    ll ans = 0;
    while (start != -1 && start < things->size()) {
        start = find(things, start, l, r);
        if (start != -1) {
            ans++;
        }
    }
    return ans;
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        ll length, l, r;
        cin >> length >> l >> r;
        things.clear();
        things.reserve(length);
        for (int i = 0; i < length; i++) {
            ll temp;
            cin >> temp;
            things.push_back(temp);
        }

        cout << solve(&things, l, r) << endl;

    }

}